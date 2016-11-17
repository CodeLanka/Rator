from __future__ import print_function
import json
import numpy as np
npa = np.array


def get_rate(semantic_string, answer):
    semantic = semantic_string.split(".")
    module = __import__('adaptors.'+".".join([semantic[0], semantic[1]]))
    submodule = getattr(module, semantic[0])
    package = getattr(submodule, semantic[1])
    adaptor = getattr(package, semantic[1].capitalize()+"Adaptor")()
    return getattr(adaptor, semantic[2])(answer)
    
def softmax(x):
    e_x = np.exp(x - np.max(x))
    out = e_x / e_x.sum()
    return out

f = open('rates_3', 'w')
with open('answers.json') as data_file:
    items = json.load(data_file)
    for item in items:
        print(item['user']['email'])
        rates = [item['user']['email'], item['user']['score']]
        for answer in item["answers"]:
            rate = get_rate(answer["semantic"], answer["value"])
            print(answer["semantic"],rate)
            rates.append(rate)
               
        rates[2:] = softmax(rates[2:])
        
        print(', '.join(list(map(str, rates))), file=f)       
        f.flush()




    


    
    
    
    
    