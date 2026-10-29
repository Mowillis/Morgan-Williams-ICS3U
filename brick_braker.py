import pygame
import random
import os

pygame.init()

# Screen Set Up
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

font = pygame.font.SysFont("Arial", 25)

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

#Ball
ball = pygame.Rect(390, 520, 18, 18)
ball_speed_x = 4
ball_speed_y = -4

#Bricks
brick_width = 65
brick_height = 28
brick_gap = 5
bricks = []
brick_colours = [RED, ORANGE, YELLOW, BLUE, PURPLE, GREEN]

def draw_game():

    screen.fill(BLACK)

    #Draw Paddle and Ball
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    #draw bricks
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    #Display Score Lives and Level
    info = font.render(
        f"Score: {score}    Lives: {lives}  Level: {level}", True, WHITE
    )
    screen.blit(info, (15,15))

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

def paddle_movement():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        paddle.x -= paddle_speed

    if keys[pygame.K_RIGHT]:
        paddle.x += paddle_speed

    if paddle.right > SCREEN_WIDTH:
        paddle.right = SCREEN_WIDTH

    if paddle.left < 0:
        paddle.left = 0

def ball_movement(ball_speed_x, ball_speed_y):

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #bounce off left and right walls
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_speed_x *= -1
        

    #bounce off roof
    if ball.top <= 0:
        ball_speed_y *= -1

    return ball_speed_x, ball_speed_y

#main game loop
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    draw_game()
    create_bricks()
    paddle_movement()

    #gets updated speeds
    ball_speed_x, ball_speed_y = ball_movement(ball_speed_x, ball_speed_y)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()