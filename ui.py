from os import system

WIDTH = 80

def print_clear_missings_inputs():
    """
        This make that user press Enter to depure all missings
        input before couting pomodoro's process.

        Doesn't work when are "Enter" character in the inputs buffer...
    """
    clear()

    print('* *'+' '*(WIDTH-6)+'* *')
    print('*'+' '*(WIDTH-2)+'*')
    print('\n'*4)
    print_position('Cleaning missings inputs.','center')
    print_position('Please press Enter...','center')
    print('\n'*3)
    print('*'+' '*(WIDTH-2)+'*')
    input('* *'+' '*(WIDTH-6)+'* *')

def get_bar(bars,pors):
    """ Returna string with the bar """
    dones = '# ' * (bars * pors//100)
    points = '_ ' * (bars - len(dones)//2)
    return '[ '+dones+points+']'

def get_input_number():
    import string
    out = input(" > ")
    aux = 'p de puta'
    if len(out) > 0:
        aux = out[0]
    if aux in string.digits and out not in string.whitespace:
        return int(out)
    else:
        return 0

def print_position(msg,position = 'left'):
    """ Print a message by a position given. The wight of aplication es 80x15"""
    space = ' '

    if   'right' in position:
        print(space*(WIDTH-len(msg))+msg)
    elif 'center' in position:
        print(space*(WIDTH//2-len(msg)//2)+msg)
    else:
        print(msg)

def print_br():
    print(" "+'- '*(WIDTH//2-1)+" ")

def clear():
    _ = system('clear')
