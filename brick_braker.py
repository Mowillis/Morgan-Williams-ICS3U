import pygame
import random
import os

pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("BRICK BREAKER")

clock = pygame.time.Clock()


#COLOURS
BLACK = (15, 15, 25)
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 70, 70)
GREEN = (50, 220, 100)
YELLOW = (255, 220, 50)
PURPLE = (180, 80, 255)
ORGANGE = (255, 150, 50)

#Player Paddle
paddle = pygame.Rect(350, 550, 100, 15)
#paddle_speed = 

def draw_game():

    screen.fill(BLACK)

    #Draw Paddle
    pygame.draw.Rect(screen, BLUE, (paddle))

#main game loop
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    draw_game()


    pygame.display.flip()
    clock.tick(60)

pygame.quit()