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

#Game Variables
score = 0
lives = 3
level = 1

#COLOURS
BLACK = (15, 15, 25)
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 70, 70)
GREEN = (50, 220, 100)
YELLOW = (255, 220, 50)
PURPLE = (180, 80, 255)
ORANGE = (255, 150, 50)

#Player Paddle
paddle = pygame.Rect(350, 550, 100, 15)
paddle_speed = 7
paddle_x = 350
#Bricks
brick_width = 65
brick_height = 20
brick_gap = 5
bricks = []
brick_colours = [RED, ORANGE, YELLOW, BLUE, PURPLE, GREEN]

def draw_game():

    screen.fill(BLACK)

    #Draw Paddle
    pygame.draw.rect(screen, WHITE, paddle)

    #draw bricks
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

def create_bricks():


    rows = 2 + level
    columns = 3 * level

    #Calculate total width
    total_width = columns * brick_width + (columns - 1) * brick_gap

    #calculate starting X
    start_x = (800 - total_width) // 2

    for row in range(rows):
        for column in range(columns):
            x = start_x + column * (brick_width + brick_gap)
            y = 65 + row * (brick_height + brick_gap)

            brick = pygame.Rect(x, y, brick_width, brick_height)
            bricks.append(brick)

def movement(paddle_x):
     keys = pygame.key.get_pressed()

     if keys[pygame.K_LEFT]:
         paddle_x = paddle_x - paddle_speed

     if keys[pygame.K_RIGHT]:
         paddle_x = paddle_x + paddle_speed
     return paddle_x
        


#main game loop
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    draw_game()
    create_bricks()
    paddle_x = movement(paddle_x)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()