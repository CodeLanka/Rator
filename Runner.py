import json

def get_rate(semantic_string, answer):
    semantic = semantic_string.split(".")
    print(semantic[1].capitalize())
    module = __import__('adaptors.'+".".join([semantic[0], semantic[1]]))
    submodule = getattr(module, semantic[0])

    package = getattr(submodule, semantic[1])
    adaptor = getattr(package, semantic[1].capitalize()+"Adaptor")()
    return getattr(adaptor, semantic[2])(answer)




with open('answers.json') as data_file:
    items = json.load(data_file)
    for item in items:
        for answer in item["answers"]:
            rate = get_rate(answer["semantic"], answer["value"])
            print(rate)
            print("end")

