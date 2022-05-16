# Pymodorner in development

import ui

PROGRAM_VERSION = '0.0.4.5.1'

def run():
    menu()

def show_app_size():
    ui.clear()
    print('* *'+' '*(ui.WIDTH-6)+'* *')
    print('*'+' '*(ui.WIDTH-2)+'*')
    print('\n'*3)
    ui.print_position('Please, resize the terminal manually.', 'center')
    ui.print_position("Terminal's dimention should be 80x15.", 'center')
    ui.print_position('You can guide by the "*" in each corner.','center')
    ui.print_position('Press Enter to go back...','center')
    print('\n'*2)
    print('*'+' '*(ui.WIDTH-2)+'*')
    input('* *'+' '*(ui.WIDTH-6)+'* *')


def menu():
    import pomodoros.classic.classic as pomo_classic

    while True:
        ui.clear()

        ui.print_position("Pymodoner in development v"+PROGRAM_VERSION+"","center")
        ui.print_br()
        print(" c. run Classic Pomodoro")
        print(" r. run Retro Pomodoro (Disable)")
        print(" s. to Configure the size of terminal manually")
        print(" q. to Exit")
        option = input("  > ")

        if   'q' in option:
            break
        elif 'c' in option:
            pomo_classic.menu()
        elif 's' in option:
            show_app_size()

run()
