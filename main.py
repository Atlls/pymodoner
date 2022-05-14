# Pymodorner in development

import ui

def run():
    menu()

def show_app_size():
    ui.clear()
    print('* *'+' '*74+'* *')
    print('*'+' '*78+'*')
    print('\n'*3)
    ui.print_position('Please, resize the terminal manually.', 'center')
    ui.print_position("Terminal's dimention should be 80x15.", 'center')
    ui.print_position('You can guide by the "*" in each corner.','center')
    ui.print_position('Press any button to go back...','center')
    print('\n'*2)
    print('*'+' '*78+'*')
    input('* *'+' '*74+'* *')


def menu():
    import pomodoros.classic.classic as pomo_classic

    while True:
        ui.clear()

        ui.read_json()
        ui.print_position("Pymodoner in development 0.0.4.4","center")
        ui.print_br()
        print("c. run Classic Pomodoro")
        print("r. run Retro Pomodoro (Disable)")
        print("s. to Configure the size of terminal manually")
        print("q. to Exit")
        option = input(" > ")

        if   'q' in option:
            break
        elif 'c' in option:
            pomo_classic.menu()
        elif 's' in option:
            show_app_size()

run()
