from os import system

def read_json():
    import json
    with open("configs/configs.json","r") as data_json:
        return json.load(data_json)

def clear():
    _ = system('clear')
