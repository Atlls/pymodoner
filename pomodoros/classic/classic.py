import ui
import app
from time import sleep

def menu():

    configs = app.read_json()

    while True:

        working, warning, shortbreak, longbreak, sessions \
        = configs["pomos"]["classic"].values()

        ui.clear()
        ui.print_position('Classic Mode Pomodoro Timer','center')
        ui.print_br()
        ui.print_position('Intervals','center')
        ui.print_position('Working : '+str(working)+' Minutes  ','right')
        ui.print_position('Working Sessions : '+str(sessions)+' Times  ','right')
        ui.print_position('Warning : '+str(warning)+' Minutes  ','right')
        ui.print_position('Break : '+str(shortbreak)+' Minutes  ','right')
        ui.print_position('Long Break : '+str(longbreak)+' Minutes  ','right')
        ui.print_br()
        print(" s. to Start session")
        print(" c. to Configure the intervals")
        print(" q. to Back main menu ")
        option = input("  > ")

        if   'q' in option:
            break
        elif 's' in option:
            run_sequense(configs)
        elif 'c' in option:
            config_menu(configs)

def config_menu(configs):

    configs_classic = configs["pomos"]["classic"]
    for config_name in configs_classic.keys():

        ui.clear()

        ui.print_position('Classic Mode Pomodoro Timer: Intervals Configuration','center')
        ui.print_br()
        print(' '+config_name.capitalize() + " time")
        print(" Current is:", configs_classic[config_name],
              "Minutes" if config_name != "sessions" else "Times")
        ui.print_br()
        print(" number. to Set minutes")
        print(" Enter.  to Skip")

        new_config = ui.get_input_number()
        if new_config:
            configs_classic[config_name] = new_config

    app.write_json(configs)

def run_sequense(configs):
    working, warning, shortbreak, longbreak, sessions\
    = configs["pomos"]["classic"].items()

    end = False
    i = 0
    sessions = sessions[1]

    # Main cicle
    while not end:

        # Working <-> Short Brack Session cicle
        while sessions > i and not end:

            (end,time_done) = start_count_post(working,"Break")
            ui.print_clear_missings_inputs()

            if not end:
                end = start_count_normal(shortbreak,\
                "Working" if sessions > i+1 else "Long Break")
                print(sessions-1,i)
                ui.print_clear_missings_inputs()
            i += 1

        if not end:
            end = start_count_normal(longbreak,"working")
            ui.print_clear_missings_inputs()

def start_count_post(interval,next_event):
    import datetime
    from time import sleep

    name, interval_time = interval
    time_now =  datetime.datetime.now()
    time_finish = time_now + datetime.timedelta(minutes=interval_time)

    end = False
    while not end and datetime.datetime.now() < time_finish:

        # Time handling
        time_running = time_finish - datetime.datetime.now()
        minutes = str(time_running)[2:7]
        bar_index = (time_running.seconds+1) / (interval_time * 60) * 100

        # Outputs
        ui.print_counting(name,minutes,bar_index)
        print(" space. to Pause the timer")
        print(" a. to Append 2 minutes at the timer")
        print(" n. to Go to",next_event)
        print(" q. to Cancel session")

        # Inputs
        if app.event_with('q'):
            end = True
        elif app.event_with('n'):
            break
        #elif ...

        # testing line
        # print(time_running.seconds,interval_time*60)
        sleep(0.06)

    time_done = 0 # Place Holder...
    return (end,time_done)

def start_count_normal(interval,next_event):
    import datetime
    from time import sleep

    name, interval_time = interval
    time_now =  datetime.datetime.now()
    time_finish = time_now + datetime.timedelta(minutes=interval_time)

    end = False
    while not end and datetime.datetime.now() < time_finish:

        # Time handling
        time_running = time_finish - datetime.datetime.now()
        minutes = str(time_running)[2:7]
        bar_index = (time_running.seconds+1) / (interval_time * 60) * 100

        # Outputs
        ui.print_counting(name,minutes,bar_index)
        print(" space. to Pause the timer")
        print(" n. to Go to",next_event)
        print(" q. to Cancel session")

        # Inputs
        if app.event_with('q'):
            end = True
        elif app.event_with('n'):
            break
        #elif ...

        # testing line
        # print(time_running.seconds,interval_time*60)
        sleep(0.06)

    return end
