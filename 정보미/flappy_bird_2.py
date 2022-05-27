import pygame
import random

pygame.init()

height = 480
width = 680
screen = pygame.display.set_mode((width, height)) 

background = pygame.image.load('C:\\Users\\buij3\\OneDrive\\바탕 화면\\pygame\\pygame_basic\\pygame_1_Galaga\\images\\background.png')

# bird
flyingbird = pygame.image.load('C:\\Users\\buij3\\OneDrive\\바탕 화면\\pygame\\pygame_basic\\pygame_1_Galaga\\images\\main_bird.png')
bird_x_pos = 200
bird_y_pos = (width / 2) - 35
to_y = 0

def display_bird(x, y):
    screen.blit(flyingbird, (x, y))

# obstacle
obstacle_1_width = 70
obstacle_1_height = random.randint(50, 150)
obstacle_1_color = (211, 253, 117)
obstacle_1_to_x = -5
obstacle_1_x_pos = width

def display_obstacle(obstacle_1_height):
    pygame.draw.rect(screen, obstacle_1_color, pygame.Rect(obstacle_1_x_pos, 0, obstacle_1_width, obstacle_1_height)) #(x축, y축, 가로, 세로)
    bottom_1_y = obstacle_1_height + 200
    bottom_1_height = bottom_1_y
    pygame.draw.rect(screen, obstacle_1_color, pygame.Rect(obstacle_1_x_pos, bottom_1_y, obstacle_1_width, bottom_1_height))

# 충돌처리
def collision_detection (obstacle_1_x_pos, obstacle_1_height, bird_y_pos, bottom_1_height):
    if obstacle_1_x_pos >= 200 and obstacle_1_x_pos <= 200:
        if bird_y_pos <= obstacle_1_height or bird_y_pos >= (bottom_1_height - 70):
            return True
    return False

running = True
waiting = True
collision = False

clock = pygame.time.Clock()

while running:
    clock.tick(68)
    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))

    while waiting:
       if collision:
            game_over()
            start()
        else:
            start()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score = 0
                    bird_y_pos = 300
                    obstacle_1_x_pos = 500
                    waiting = False

            if event.type == pygame.QUIT:
                waiting = False
                running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                to_y -= 6

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                to_y += 3
    bird_y_pos += to_y
    if bird_y_pos <= 0:
        bird_y_pos = 0
    if bird_y_pos >= height:
        bird_y_pos = height
        
    obstacle_x_pos += obstacle_to_x

    collision = collision_detection(obstacle_1_x_pos, obstacle_1_height, bird_y_pos, obstacle_1_height + 150)

    if collision:
        score_list.append(score)
        waiting = True

    if obstacle_x_pos <= -10:
        obstacle_x_pos = 500
        obstacle_height = random.randint(200, 400)
        score += 1
        
    display_obstacle(obstacle_1_height)

    display_bird(bird_x_pos, bird_y_pos)

    pygame.display.update()
    
pygame.quit()
