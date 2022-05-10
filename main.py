# Pymodorer in development

def read_json():
    import json
    with open("configs/configs.json","r") as data_json:
        print(json.load(data_json))

def run():
    menu()

def menu():
    import ui, pomodoros.classic.classic as pomo_classic

    while True:
        ui.clear()
        print("Pymodoner in development 0.0.1")
        print("Menu")
        print("c. Classic Pomodoro")
        print("r. Retro Pomodoro")
        print("q. Exit")
        option = input(" > ")

        if   'q' in option:
            break
        elif 'c' in option:
            pomo_classic.run(60*10)

read_json()
#run()
