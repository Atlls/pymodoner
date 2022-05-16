import keyboard as kb
import ui
import app
from time import sleep

def exp1():
    impreso = False
    while not impreso:
        sleep(0.1)
        if kb.is_pressed("q"):
            print("q")
            impreso = True
        else:
            print(".\n")

def exp2():
    import keyboard  # using module keyboard
    while True:  # making a loop

        # used try so that if user pressed other than 
        # the given key error will not be shown
        try:
            if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                print('You Pressed A Key!')
                break  # finishing the loop
            else:
                print('.')
        except:
            # if user pressed a key other than the given key the loop will break
            break
        sleep(0.1)

def exp3():
    import keyboard

    while True:

        try:
            if keyboard.read_key() == "p":
                print("You pressed p")
                break
            else:
                print('.')
        except:
            break


def exp4():
    import sys
    import time

    for i in range(10):
        print(i, end=" ",flush=True)
        time.sleep(1)

def start_count(interval,warning=0):
    import keyboard # Requiere sudo
    import datetime
    from time import sleep
    time_now =  datetime.datetime.now()
    time_finish = time_now + datetime.timedelta(seconds=interval)

    flag = False
    while not flag and datetime.datetime.now() < time_finish:
        ui.clear()
        print(time_finish - datetime.datetime.now())
        print(datetime.datetime.now() < time_finish)

        if app.event_with('q'):
            flag = True
        sleep(0.075)


def exp5():
    import keyboard
    import time
    a = int(input("Enter the time (in seconds) for which you want to disable keyboard: "))
    for i in range(150):
        keyboard.block_key(i)
    time.sleep(a)
    input("   >  .")
exp5()
