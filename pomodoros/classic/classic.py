import ui
import app
from time import sleep

def menu():

    configs = app.read_json()

    while True:

        working, warning, shortbreak, longbreak \
        = configs["pomos"]["classic"].values()

        ui.clear()
        ui.print_position('Classic Mode Pomodoro Timer','center')
        ui.print_br()
        ui.print_position('Intervals','center')
        ui.print_position('Working : '+str(working)+' Minutes  ','right')
        ui.print_position('Warning : '+str(warning)+' Minutes  ','right')
        ui.print_position('Break : '+str(shortbreak)+' Minutes  ','right')
        ui.print_position('Long Break : '+str(longbreak)+' Minutes  ','right')
        ui.print_br()
        print(" s. to Start session")
        print(" c. to Configure the intervals")
        print(" q. to Back main menu ")
        # Another input to get all trash from start_count?
        option = input("  > ")

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

    app.write_json(configs)

def run_sequense(configs):
    working, warning, shortbreak, longbreak \
    = configs["pomos"]["classic"].items()

    start_count(working)

    ui.print_clear_missings_inputs()

def start_count(interval,warning=0):
    import datetime
    from time import sleep

    name_time, interval_time = interval
    time_now =  datetime.datetime.now()
    time_finish = time_now + datetime.timedelta(minutes=interval_time)

    flag = False
    while not flag and datetime.datetime.now() < time_finish:

        # Time manipuling
        time_running = time_finish - datetime.datetime.now()
        minutes = str(time_running)[2:7]
        porcentage_bar = (time_running.seconds+1) / (interval_time * 60) * 100

        # Outputs
        ui.clear()
        ui.print_position('Classic Mode Pomodoro Timer: Running Session','center')
        ui.print_br()
        print('\n')
        print(" in", name_time.capitalize(),"time...")
        ui.print_position("- "+minutes+" -",'center')
        ui.print_position(ui.get_bar(20,int(porcentage_bar)),'center')
        print('\n')
        ui.print_br()
        print(" space. to Pause the timer")
        print(" a. to Append 2 minutes at the timer")
        print(" n. to Go to","*place holder*")
        print(" q. to Cancel session")

        # Inputs
        if app.event_with('q'):
            flag = True

        # testing line
        # print(time_running.seconds,interval_time*60)
        sleep(0.075)


# COMMING TO DELETE #
def start_count_old(interval,warning = 0):
    import keyboard # Requiere sudo
    from datetime import timedelta
    name_time, interval_time = interval

    time_finish = timedelta(minutes=interval_time)
    time_running = time_finish

    cancel = False

    ui.clear()

    while  time_running.total_seconds() > 0 and not cancel:

        sleep(0.1)

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
        print(" q. to Cancel session")
        print(" a. to Put 5 minutes more")
        print(" space. to Pause the timer")

        if keyboard.is_pressed('q'):
            cancel = True
            # ! Disabl Keyboard?

        # Clear buffer

