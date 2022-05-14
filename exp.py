from time import sleep
import ui

def get_bar(bars,pors):
    dones = '# ' * (bars * pors//100)
    points = '- ' * (bars - len(dones)//2)
    return '[ '+dones+points+']'

def print_position(msg,position = 'left'):

    space = ' '

    if   'right' in position:
        print(space*(80-len(msg))+msg)
    elif 'center' in position:
        print(space*(40-len(msg)//2)+msg)
    else:
        print(msg)


msg = "Me cago en las putas"
print_position(msg,'right')
print_position(msg,'center')
print_position(get_bar(10,100),'center')

for i in range(1,101):
    print_position(msg,'left')
    print_position(get_bar(20,i),'center')
    sleep(0.1)
    ui.clear()
