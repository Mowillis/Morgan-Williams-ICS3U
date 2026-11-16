import pygame
import random

pygame.init()

#make random sounds
sounds = [
    pygame.mixer.Sound("contact_sound.mp3")
    ]

# Set screen dimensions
# Screen Set Up
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

font = pygame.font.SysFont("Arial", 25)
big_font = pygame.font.SysFont("Arial", 45)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("BRICK BREAKER")

clock = pygame.time.Clock()

#Game Variables
score = 0
lives = 3
level = 1
game_state = "menu"
title = ""
message = ""

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

#Ball
ball = pygame.Rect(390, 520, 18, 18)
ball_speed_x = 6
ball_speed_y = -6

#Bricks
brick_width = 65
brick_height = 20
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

    #prints bricks centered
    for row in range(rows):
        for column in range(columns):
            x = start_x + column * (brick_width + brick_gap)
            y = 65 + row * (brick_height + brick_gap)

            brick = pygame.Rect(x, y, brick_width, brick_height)
            bricks.append(brick)

def paddle_movement(paddle_x):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        paddle.x -= paddle_speed

    if keys[pygame.K_RIGHT]:
        paddle.x += paddle_speed

    if keys[pygame.K_LEFT]:
         paddle_x = paddle_x - paddle_speed
    if paddle.right > SCREEN_WIDTH:
        paddle.right = SCREEN_WIDTH

    if keys[pygame.K_RIGHT]:
         paddle_x = paddle_x + paddle_speed
    if paddle.left < 0:
        paddle.left = 0

    return paddle_x

def check_collison(ball_speed_x, ball_speed_y, score):
    if ball.colliderect(paddle) and ball_speed_y > 0:
        #makes ball not go through paddle
        ball.bottom = paddle.top
        ball_speed_y *= -1

        #change ball direction depending where ball hits paddle
        hit_position = (ball.centerx - paddle.centerx) / (paddle.width / 2)
        ball_speed_x = int(hit_position * 5)

        if ball_speed_x == 0:
            ball_speed_x = random.choice ([6,-6])
        random.choice(sounds).play()


    brick_hit = False

    #makes ball bounce back smoothly and change derection depending where hit
    for brick in bricks:
        if ball.colliderect(brick) and brick_hit == False:

            if old_ball.right <= brick.left:
                ball_speed_x = -ball_speed_x
                ball.x = old_ball.x
            
            elif old_ball.left >= brick.right:
                ball_speed_x = -ball_speed_x
                ball.x = old_ball.x
                
            elif old_ball.bottom <= brick.top:
                ball_speed_y = -ball_speed_y
                ball.y = old_ball.y
                
            elif old_ball.top >= brick.bottom:
                ball_speed_y = -ball_speed_y
                ball.y = old_ball.y
                
            bricks.remove(brick)
            score += 10
            brick_hit = True
            random.choice(sounds).play()

    return ball_speed_x, ball_speed_y, score

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

def reset_ball(ball_speed_x, ball_speed_y):
    #return ball and paddle to starting position
    paddle.x = SCREEN_WIDTH // 2 - paddle.width // 2
    ball.x = SCREEN_WIDTH // 2 - ball.width // 2
    ball.y = SCREEN_HEIGHT - 80

    ball_speed_x = random.choice ([4,-4])
    ball_speed_y = -4

    return ball_speed_x, ball_speed_y

def draw_message(title, message):
    #clears screen and displays message
    screen.fill(BLACK)
    title_display = big_font.render(title, True, YELLOW)
    message_display = font.render(message, True, WHITE)

    screen.blit(title_display, (SCREEN_WIDTH // 2 - title_display.get_width() // 2, 220
))
    screen.blit(message_display, (SCREEN_WIDTH // 2 - message_display.get_width() // 2, 300
))
    return title, message

def reset_game(score, lives, level):
    score = 0
    lives = 3
    level = 1

    create_bricks()
    reset_ball(ball_speed_x, ball_speed_y)

    return score, lives, level

        
create_bricks()
reset_ball(ball_speed_x, ball_speed_y)

#main game loop
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    if game_state == "playing":

        draw_game()
        paddle_movement(paddle_x)
        #used to make new ball when colision with bricks
        old_ball = ball.copy()
        ball_speed_x, ball_speed_y = ball_movement(ball_speed_x, ball_speed_y)
        ball_speed_x, ball_speed_y, score = check_collison(ball_speed_x, ball_speed_y, score)

        #reset ball and lose life if ball falls bellow paddle
        if ball.top > SCREEN_HEIGHT:
            reset_ball(ball_speed_x, ball_speed_y)
            lives -= 1

            #end game when lives = 0
            if lives <= 0:
                game_state = "game over"

        #Makes second level start
        if len(bricks) == 0:
            if level < 3:
                level += 1
                create_bricks()
                reset_ball(ball_speed_x, ball_speed_y)
            
            elif len(bricks) == 0 and level >= 3:
                game_state = "victory"
                
#displays different screens depending on game state
    if game_state == "menu":
        title = "BRICK BREAKER"
        message = "Press RETURN to start, ESC to quit"
        title, message = draw_message(title, message)
    
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_RETURN]:
            game_state = "playing"

        if keys[pygame.K_ESCAPE]:
            running = False

    if game_state == "game over":
        title = "GAME OVER"
        message = "Press RETURN to restart, ESC to quit"
        title, message = draw_message(title, message)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            score, lives, level = reset_game(score, lives, level)
            game_state = "playing"

        if keys[pygame.K_ESCAPE]:
            running = False

    if game_state == "victory":
        title = "VICTORY!"
        message = "You Cleared All 3 Levels!"
        title, message = draw_message(title, message)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()