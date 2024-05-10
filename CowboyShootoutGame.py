import os
import time
import random
import platform
import keyboard

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def wait_for_keypress(target):
    while True:
        if keyboard.is_pressed(str(target)):
            return True
        time.sleep(0.1)

clear_screen()

target = random.randint(1, 9)

print('COWBOY SHOOTOUT'
      '\n' 'YOU ARE BACK TO BACK'
      '\n' 'TAKE 10 PACES...')

for i in range(1, 11):
    time.sleep(0.5)
    print(i, '...')

sleep_time = random.randint(1, 5)
time.sleep(sleep_time)
print('HE DRAWS...')

if wait_for_keypress(target):
    print('BUT YOU SHOOT FIRST'
          '\n' 'YOU KILLED HIM')
else:
    print('AND SHOOTS'
          '\n' 'YOU ARE DEAD')