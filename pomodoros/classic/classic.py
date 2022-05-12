import ui

def menu():

    configs = ui.read_json()

    while True:

        ui.clear()
        print("Classic Pomodoro timer")
        print("")
        print("s. to Start session")
        print("c. to Configure the intervals")
        print("q. to Back last menu ")
        option = input(" > ")

        if   'q' in option:
            break
        elif 's' in option:
            run_sequense(configs)
        elif 'c' in option:
            config_menu(configs)

# ui?
def config_menu(configs):

    configs_classic = configs["pomos"]["classic"]
    for config_name in configs_classic.keys():

        ui.clear()

        print(" of",config_name.capitalize() + "'s time")
        print(" current is:", configs_classic[config_name],"minutes")
        print(" number. to Set new value")
        print(" Enter.  to Skip")
        new_config = ui.get_input()
        if new_config:
            configs_classic[config_name] = new_config

    ui.write_json(configs)

def run_sequense(configs):
    working, warning, shortbreak, longbreak \
    = configs["pomos"]["classic"].values()

    start_count(working)

def start_count(interval,warning = 0):
    import keyboard # Requiere sudo
    from time import sleep
    from datetime import timedelta

    time_finish = timedelta(minutes=interval)

    while  time_finish.total_seconds() > 0:
        ui.clear()
        time_finish -= timedelta(seconds=1)

        print(str(time_finish)[2:7])
        print("q. to Go Classic's menu")

        event = keyboard.read_event()

        if 'q' in event.name:
            break
        sleep(1)
