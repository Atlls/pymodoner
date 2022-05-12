# Pymodorner in development

import ui

def run():
    menu()

def menu():
    import pomodoros.classic.classic as pomo_classic

    while True:
        ui.clear()

        ui.read_json()
        print("Pymodoner in development 0.0.4")
        print("Menu")
        print("c. Classic Pomodoro")
        print("r. Retro Pomodoro")
        print("q. Exit")
        option = input(" > ")

        if   'q' in option:
            break
        elif 'c' in option:
            pomo_classic.menu()

run()
