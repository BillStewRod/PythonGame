import pygame
import sys
import time
import random

# Initialize Pygame
pygame.init()

# Set up the window dimensions
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 200
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set up the title of the window
pygame.display.set_caption('Cowboy Shootout')

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the font
font = pygame.font.SysFont(None, 30)

# Define the target number
target = random.randint(1, 9)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == str(target):
                print('BUT YOU SHOOT FIRST')
                print('YOU KILLED HIM')
                pygame.quit()
                sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Print the game text
    text = font.render('COWBOY SHOOTOUT\nYOU ARE BACK TO BACK\nTAKE 10 PACES...', True, WHITE)
    screen.blit(text, (10, 10))

    # Update the screen
    pygame.display.flip()

    # Wait for 10 seconds
    time.sleep(10)

    # Print the opponent's draw
    text = font.render('HE DRAWS...', True, WHITE)
    screen.blit(text, (10, 100))
    pygame.display.flip()

    # Wait for a random amount of time
    sleep_time = random.randint(1, 5)
    time.sleep(sleep_time)

    # Print the opponent's shot
    text = font.render('AND SHOOTS\nYOU ARE DEAD', True, WHITE)
    screen.blit(text, (10, 150))
    pygame.display.flip()

    # Wait for a key press
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                break