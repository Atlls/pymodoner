import ui

def menu():

    configs = ui.read_json()

    while True:

        ui.clear()
        print(configs)
        print("Classic Pomodoro timer")
        print("Menu")
        print("s. to Start session")
        print("c. to Configure the intervals")
        print("q. to Back last menu ")
        option = input(" > ")

        if   'q' in option:
            break
        elif 's' in option:
            run(configs["pomos"]["classic"]['working'])
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


def run(interval):
    from time import sleep
    from datetime import timedelta

    time_finish = timedelta(minutes=interval)

    while  time_finish.total_seconds() > 0:

        ui.clear()
        time_finish -= timedelta(seconds=1)
        print(str(time_finish)[2:7])
        sleep(1)
        ui.clear()
