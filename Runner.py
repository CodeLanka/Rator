from __future__ import print_function
import json
import numpy as np


def get_rate(semantic_string, answer):
    semantic = semantic_string.split(".")
    if len(semantic) > 1:
        module = __import__('adaptors.'+".".join([semantic[0], semantic[1]]))
        submodule = getattr(module, semantic[0])
        package = getattr(submodule, semantic[1])
        adaptor = getattr(package, semantic[1].capitalize()+"Adaptor")()
        return getattr(adaptor, semantic[2])(answer)
    else:
        return None
    

def soft_max(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)


def soft_max_2(x):
    e_x = np.exp(x - np.max(x))
    out = e_x / e_x.sum()
    return out


def apply_soft_max(rate_list):
    for rateIndex in range(len(rate_list)):
        rate_list[rateIndex] = list(soft_max_2(rate_list[rateIndex]))


def merge_user_rate(user_array, rate_array):
    for userIndex in range(len(user_array)):
        for rateIndex in range(len(rate_array)):
            user_array[userIndex].append(rate_array[rateIndex][userIndex])


def write_results(final_array):
    f = open('rates_123', 'w')
    print('\n'.join(list(map(lambda s: ", ".join(list(map(str, s))), final_array))), file=f)
    print('\n'.join(list(map(str, final_array))))
    f.flush()


with open('data/answers_prod.json') as data_file:
    items = json.load(data_file)
    rate_array = []
    user_array = []

    for answer in items[0]['answers']:
        rate_array.append([])

    for item in items:
        user = [item['user']['email'], item['user']['score']]
        user_array.append(user)
        for idx, answer in enumerate(item["answers"]):
            rate = get_rate(answer["semantic"], answer["answer"])
            if rate is not None:
                print(" - ",answer["semantic"], ":", rate)
                # rates.append(rate)
                rate_array[idx].append(rate)
            else:
                print("non-sem")

    apply_soft_max(rate_array)
    merge_user_rate(user_array, rate_array)
    write_results(user_array)


