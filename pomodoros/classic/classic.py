import ui

def menu():

    configs = ui.read_json()
    configs = dict(configs['pomos']['classic'].items())

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
            run(configs['working'])
        elif 'c' in option:
            # Configation of json
            break


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
