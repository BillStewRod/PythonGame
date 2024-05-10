from time import sleep
from random import randint
import os
import subprocess
import sys
import termios
import tty

def clear_screen():
    if os.name == 'nt':  # Check if running on Windows
        _ = subprocess.call('cls')
    else:  # Assumes macOS/Linux 
        _ = subprocess.call('clear')

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

clear_screen()

target = randint(1, 9)  # Assuming number keys for aiming

print('COWBOY SHOOTOUT'
        '\n' 'YOU ARE BACK TO BACK'
        '\n' 'TAKE 10 PACES...')

W = 1
while W <= 10:
    sleep(0.5)
    print(W, '...')
    W += 1

S = randint(1, 5)
sleep(S)
print('HE DRAWS...')

X = 0
while X < S:
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        key_pressed = ord(getch()) - 48  # Convert key press to number
        if key_pressed == target:
            print('BUT YOU SHOOT FIRST'
                  '\n' 'YOU KILLED HIM')
            exit()
        else:
            print('YOU MISSED!')
    else:
        sleep(0.5)
        X += 1

print('AND SHOOTS'
      '\n' 'YOU ARE DEAD')
