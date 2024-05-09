from time import sleep 
from random import randint 
import msvcrt 
import os
import subprocess

def clear_screen():
    if os.name == 'nt':  # Check if running on Windows
        _ = subprocess.call('cls')
    else:  # Assumes macOS/Linux 
        _ = subprocess.call('clear')

clear_screen() 

target = randint(1, 9)  # Assuming number keys for aiming

print('COWBOY SHOOTOUT'
        '\n''YOU ARE BACK TO BACK'
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
    if msvcrt.kbhit() == True:
        try:
            key_pressed = ord(msvcrt.getch()) - 48  # Convert key press to number
            if key_pressed == target:
                print('BUT YOU SHOOT FIRST'
                        '\n' 'YOU KILLED HIM')
                exit()
            else:
                print('YOU MISSED!')
        except ValueError:
            print("Press a number key to aim!")
    else:
        sleep (0.5)
        X = X + 1

print(' AND SHOOTS'
'\n''YOU ARE DEAD')