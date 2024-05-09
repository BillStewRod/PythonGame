import os
import random
import string
import time

def clear_screen():
    # Clear the terminal screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

print('VITAL MESSAGE\n')

difficulty = 0
while True:
    try:
        difficulty = int(input('HOW DIFFICULT? (4-10)'))
        if 4 <= difficulty <= 10:
            break
    except ValueError:
        print("Invalid input. Please enter an integer between 4 and 10.")

message = ''.join(random.choice(string.ascii_uppercase) for _ in range(difficulty))

clear_screen()

print('SEND THIS MESSAGE:\n\n', message)

time.sleep(0.5 * difficulty)

clear_screen()

user_input = input('')

if user_input == message:
    print('MESSAGE CORRECT\n\nTHE WAR IS OVER')
else:
    print('YOU GOT IT WRONG\nYOU SHOULD HAVE SENT:\n', message)
