import pygame
import os
import random

pygame.init() # 초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Galaga") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 초기 세팅
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경 만들기
background  = pygame.image.load(os.path.join(image_path, "galaga_background.png"))

# 캐릭터 불러오기
character = pygame.image.load("C:\\Users\\buij3\\OneDrive\\바탕 화면\\pygame\\pygame_basic\\pygame_1_Galaga\\images\\main_sprite.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기의 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 적 enemy 캐릭터
bug1 = pygame.image.load("C:\\Users\\buij3\\OneDrive\\바탕 화면\\pygame\\pygame_basic\\pygame_1_Galaga\\images\\main_enemy_bug3.png")
bug1_size = bug1.get_rect().size # 이미지의 크기를 구해옴
bug1_width = bug1_size[0] # 캐릭터의 가로 크기
bug1_height = bug1_size[1] # 캐릭터의 세로 크기
bug1_x_pos = (screen_width / 2) - (bug1_width / 2) # 화면 가로의 절반 크기의 해당하는 곳에 위치
bug1_y_pos = (screen_height / 2) - (bug1_height / 2) # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 캐릭터 이동할 좌표
to_x = 0

# 캐릭터 이동 속도
character_speed = 0.8

# 무기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

weapons = []

# 무기 이동 속도
weapon_speed = 10

# 이벤트 루프
running = True # 게임이 진행중인가?/ 프로그램이 종료되지 않도록
while running:
    dt = clock.tick(60)

    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= 5 # to_x = to_x - 5
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += 5
            elif event.key == pygame.K_SPACE: # 무기 발사
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

        


    character_x_pos += to_x

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons] # 무기 위치를 위로

    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]


    screen.blit(background, (0, 0)) # 배경 그리기

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(bug1, (bug1_x_pos, bug1_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기!

# pygame 종료
pygame.quit()

