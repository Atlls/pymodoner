from time import sleep
from datetime import timedelta

def run(interval):
    import ui
    time_finish = timedelta(seconds=interval)
    while  time_finish.total_seconds() > 0:
        ui.clear()
        time_finish -= timedelta(seconds=1)
        print(str(time_finish)[2:7])
        sleep(1)
        ui.clear()
