from __future__ import print_function
import json


def get_rate(semantic_string, answer):
    semantic = semantic_string.split(".")
    module = __import__('adaptors.'+".".join([semantic[0], semantic[1]]))
    submodule = getattr(module, semantic[0])

    package = getattr(submodule, semantic[1])
    adaptor = getattr(package, semantic[1].capitalize()+"Adaptor")()
    return getattr(adaptor, semantic[2])(answer)

with open('answers.json') as data_file:

    items = json.load(data_file)
    a = 0
    
    for item in items:
        github = 0
        so = 0

        for answer in item["answers"]:
            if answer["semantic"] == "user.github.username" and answer["value"] != "":
                github += 1
            elif answer["semantic"] == "user.stackoverflow.url" and answer["value"] != "":
                so += 1
        if github == 1 and so == 1:
            a += 1
    print(a)


