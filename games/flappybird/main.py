import pygame
import random
import os, sys

def gameStart():
    pygame.init()

    height = 720
    width = 720
    screen = pygame.display.set_mode((width, height))  # 화면 세팅

    currentPath_bg = os.path.dirname(__file__)
    currentPath_bg = os.path.join(currentPath_bg, 'background.png')
    background = pygame.image.load(currentPath_bg)

    # 새
    currentPath_fb = os.path.dirname(__file__)
    currentPath_fb = os.path.join(currentPath_fb, 'main_bird.png')
    flyingbird = pygame.image.load(currentPath_fb)
    character_size = flyingbird.get_rect().size # 이미지의 크기를 구해옴
    character_width = character_size[0] # 캐릭터의 가로 크기
    character_height = character_size[1] # 캐릭터의 세로 크기
    bird_x_pos = 150
    bird_y_pos = (width / 2) - 40
    to_y = 0

    def display_bird(x, y):
        screen.blit(flyingbird, (x, y))

    # 장애물
    obstacle_1_width = 80
    obstacle_1_height = random.randint(100, 300)
    obstacle_1_color = (211, 253, 117)
    obstacle_1_to_x = -4
    obstacle_1_x_pos = 400
    bottom_1_y = obstacle_1_height + 200

    obstacle_2_width = 80
    obstacle_2_height = random.randint(100, 300)
    obstacle_2_color = (211, 253, 117)
    obstacle_2_to_x = -4
    obstacle_2_x_pos = width
    bottom_2_y = obstacle_2_height + 200

    def display_obstacle1(obstacle_1_height):
        pygame.draw.rect(screen, obstacle_1_color, pygame.Rect(obstacle_1_x_pos, 0, obstacle_1_width, obstacle_1_height)) #(x축, y축, 가로, 세로)
        bottom_1_y = obstacle_1_height + 200
        #bottom_1_height = bottom_1_y
        pygame.draw.rect(screen, obstacle_1_color, pygame.Rect(obstacle_1_x_pos, bottom_1_y, obstacle_1_width, height))

    # 장애물2
    def display_obstacle2(obstacle_2_height):
        pygame.draw.rect(screen, obstacle_2_color, pygame.Rect(obstacle_2_x_pos, 0, obstacle_2_width, obstacle_2_height)) #(x축, y축, 가로, 세로)
        bottom_2_y = obstacle_2_height + 200
        #bottom_1_height = bottom_1_y
        pygame.draw.rect(screen, obstacle_2_color, pygame.Rect(obstacle_2_x_pos, bottom_2_y, obstacle_2_width, height))

    # 충돌처리
    def collision_detection1(obstacle_1_x_pos, obstacle_1_height, bird_y_pos, bottom_1_y):
        if bird_x_pos == obstacle_1_x_pos:
            return True
        elif 150 <= obstacle_1_x_pos <= (150 + 80): # 기둥 사이에 있을 때:
            if obstacle_1_x_pos == bird_x_pos:
                return True
            if bird_y_pos == obstacle_1_height or bird_y_pos >= bottom_1_y:
                return True
        return False

    def collision_detection2(obstacle_2_x_pos, obstacle_2_height, bird_y_pos, bottom_2_y):
        if bird_x_pos == obstacle_2_x_pos:
            return True
        elif 150 <= obstacle_2_x_pos <= (150 + 80): # 기둥 사이에 있을 때:
            if obstacle_2_x_pos == bird_x_pos:
                return True
            if bird_y_pos == obstacle_2_height or bird_y_pos >= bottom_2_y:
                return True
        return False

    # 점수
    score = 0
    font_score = pygame.font.Font('freesansbold.ttf', 32)

    def score_display(score):
        display = font_score.render(f"Score: {score}", True, (255,255,255))
        screen.blit(display, (10, 10))

    # 시작 글씨
    font_start = pygame.font.Font('freesansbold.ttf', 50)
    def start():
        display = font_start.render(f"Game Start: space bar", True, (255, 255, 255))
        screen.blit(display, (90, 200))
        pygame.display.update()

    # 게임 오버 글씨
    score_list = [0]

    font1_gameover = pygame.font.Font('freesansbold.ttf', 80)
    font2_score = pygame.font.Font('freesansbold.ttf', 40)

    def gameover():

        maxscore = max(score_list)
        display1 = font1_gameover.render(f"Game Over", True, (200,35,35))
        screen.blit(display1, (145, 350))
        display2 = font2_score.render(f"score: {score} 1ST: {maxscore}", True, (255, 255, 255))
        screen.blit(display2, (220, 600))

    running = True
    waiting = True
    collision1 = False
    collision2 = False ##

    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        while waiting:
            if collision1 == True or collision2 == True:
                gameover()
                start()
            else:
                start()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        score = 0
                        bird_y_pos = (width / 2) - 40
                        obstacle_1_x_pos = 400
                        obstacle_2_x_pos = width
                        waiting = False

                if event.type == pygame.QUIT:
                    waiting = False
                    running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    to_y -= 4   
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    to_y += 2
   

        bird_y_pos += to_y
 
        # 경계값 처리
        if bird_y_pos <= 0:
            bird_y_pos = 0
        if bird_y_pos >= height:
            bird_y_pos = height - character_height 

    # 장애물 움직이기
        obstacle_1_x_pos += obstacle_1_to_x
        obstacle_2_x_pos += obstacle_2_to_x

        # 충돌
        collision1 = collision_detection1(obstacle_1_x_pos, obstacle_1_height, bird_y_pos, bottom_1_y)
        collision2 = collision_detection2(obstacle_2_x_pos, obstacle_2_height, bird_y_pos, bottom_2_y)
                
        if collision1 or collision2 :
            score_list.append(score)
            waiting = True

        # 새롭게 장애물 만들기
        if obstacle_1_x_pos <= -10:
            obstacle_1_x_pos = width
            obstacle_1_height = random.randint(100, 300)
            score += 1

        if obstacle_2_x_pos <= -10:
            obstacle_2_x_pos = width
            obstacle_2_height = random.randint(100, 300)
            score += 1

        display_obstacle1(obstacle_1_height)
        display_obstacle2(obstacle_2_height)
        display_bird(bird_x_pos, bird_y_pos)
        score_display(score)

        pygame.display.update()

    pygame.quit()
gameStart()
