import ui
import app

def menu():

    configs = ui.read_json()

    while True:

        ui.clear()
        ui.print_position('Classic Mode Pomodoro Timer','center')
        ui.print_br()
        print("s. to Start session")
        print("c. to Configure the intervals")
        print("q. to Back main menu ")
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

        ui.print_position('Classic Mode Pomodoro Timer: Intervals Configuration','center')
        ui.print_br()
        print(' '+config_name.capitalize() + " time")
        print(" Current is:", configs_classic[config_name],"minutes")
        ui.print_br()
        print(" number. to Set minutes")
        print(" Enter.  to Skip")

        new_config = ui.get_input_number()
        if new_config:
            configs_classic[config_name] = new_config

    ui.write_json(configs)

def run_sequense(configs):
    working, warning, shortbreak, longbreak \
    = configs["pomos"]["classic"].items()

    start_count(working)

def start_count(interval,warning = 0):
    from time import sleep
    from datetime import timedelta
    name_time, interval_time = interval

    time_finish = timedelta(minutes=interval_time)
    time_running = time_finish

    while  time_running.total_seconds() > 0:
        ui.clear()
        time_running -= timedelta(seconds=1)

        ui.print_position('Classic Mode Pomodoro Timer: Running Session','center')
        ui.print_br()
        print('\n')
        print(" in", name_time,"time...")
        minutes = str(time_running)[2:7]
        ui.print_position("- "+minutes+" -",'center')
        porcentage_bar = (time_running.seconds+1) / time_finish.seconds * 100
        #print(time_running.seconds,time_finish.seconds)
        ui.print_position(ui.get_bar(20,int(porcentage_bar)),'center')
        print('\n')
        ui.print_br()
        print("q. to Cancel session")

        sleep(1)
