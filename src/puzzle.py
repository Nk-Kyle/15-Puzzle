import numpy as np
from colorama import Fore, Style

def read():
    f = open(input("Nama File (Ex : ../test/in1.txt): "), 'r')
    mat = [[int(val) for val in line.split()] for line in f]
    validate(mat)
    return mat

def random():
    base = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    np.random.shuffle(base)
    base = np.reshape(base,(4,4))
    return base

def validate(mat):
    tester = [False for i in range(16)]
    for i in range(4):
        for j in range(4):
            tester[mat[i][j]-1] = True
    for status in tester:
        if (not(status)):
            raise Exception("Configuration Not Valid!")




# unicode for draw puzzle in command promt or terminal
left_down_angle = '\u2514'
right_down_angle = '\u2518'
right_up_angle = '\u2510'
left_up_angle = '\u250C'

middle_junction = '\u253C'
top_junction = '\u252C'
bottom_junction = '\u2534'
right_junction = '\u2524'
left_junction = '\u251C'

#bar color
bar = Style.BRIGHT + Fore.CYAN + '\u2502' + Fore.RESET + Style.RESET_ALL
dash = '\u2500'
dashes = dash + dash + dash + dash
first_line = Style.BRIGHT + Fore.CYAN + left_up_angle + dashes + top_junction + dashes + top_junction + dashes+ top_junction + dashes+  right_up_angle + Fore.RESET + Style.RESET_ALL
middle_line = Style.BRIGHT + Fore.CYAN + left_junction + dashes + middle_junction + dashes + middle_junction + dashes + middle_junction + dashes + right_junction + Fore.RESET + Style.RESET_ALL
last_line = Style.BRIGHT + Fore.CYAN + left_down_angle + dashes + bottom_junction + dashes + bottom_junction + dashes+ bottom_junction + dashes+  right_down_angle + Fore.RESET + Style.RESET_ALL

#puzzle print function
def print_puzzle(array):
    print(first_line)
    for a in range(len(array)):
        for i in array[a]:
            if (i < 16):
                if (i < 10):
                    print(bar + ' ', end = '')
                else:
                    print(bar, end='')
                print(' ' + str(i), end=' ')
            else:
                print(bar + '   ', end = ' ')

        print(bar)
        if a == 3:
            print(last_line)
        else:
            print(middle_line)
