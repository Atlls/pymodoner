from os import system

def get_input():
    import string
    out = input(" > ")
    if out in string.digits and out not in string.whitespace:
        return int(out)
    else:
        return 0

def read_json():
    import json
    with open("configs/configs.json","r") as data_json:
        return json.load(data_json)

def write_json(data):
    import json
    with open("configs/configs.json","w") as outfile:
        json.dump(data,outfile)

def clear():
    _ = system('clear')
