import keyboard # Requiere sudo

def read_json():
    import json
    with open("configs/configs.json","r") as data_json:
        return json.load(data_json)

def write_json(data):
    import json
    with open("configs/configs.json","w") as outfile:
        json.dump(data,outfile)


def event_with(key):
    import keyboard
    try:
        if keyboard.is_pressed(key): # This, Requiere sudo
            return True
    except:
        return False
