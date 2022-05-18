import pygame
import random

pygame.init()

background = pygame.display.set_mode((500, 800))
pygame.display.set_caption("Brick Breaker")


# 배경 사이즈
size_width_bg = background.get_size()[0]
size_height_bg = background.get_size()[1]


# 페달의 사이즈, 좌표, Rect(모든 좌표를 모아서 갖고 있는 변수)
size_width_pedal = 100 
size_height_pedal = 15

x_pos_pedal = size_width_bg // 2 - size_width_pedal // 2
y_pos_pedal = size_height_bg - size_height_pedal

rect_pedal = pygame.Rect(x_pos_pedal, y_pos_pedal, size_width_pedal, size_height_pedal)

to_x_pedal = 0  # to_x


# 공의 사이즈, 좌표, Rect
size_radius_ball = 20

x_pos_ball = size_width_bg // 2
y_pos_ball = size_height_bg - size_height_pedal - size_radius_ball

rect_ball = pygame.Rect(x_pos_ball, y_pos_ball, size_radius_ball*2, size_radius_ball*2)
rect_ball.center = (x_pos_ball, y_pos_ball)

# 공의 방향과 스피드
x_speed_ball = 0.1  
y_speed_ball = 0.1

# 블록 사이즈, 좌표, Rect
size_width_block = size_width_bg // 10
size_height_block = 30

x_pos_block = 0
y_pos_block = 0

rect_block = [[] for _ in range(10)]
color_block = [[] for _ in range(10)]

for i in range(10):
    for j in range(3):
        rect_block[i].append(pygame.Rect(i*size_width_block, j*size_height_block, size_width_block, size_height_block))
        color_block[i].append((random.randrange(255), random.randrange(150, 255), random.randrange(150, 255)))  # 컬러값을 랜덤으로 뽑음


# 마우스 좌표
x_pos_mouse, y_pos_mouse = 0, 0


play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        # 마우스로 페달 움직이기
        if event.type == pygame.MOUSEMOTION:
            x_pos_mouse, y_pos_mouse = pygame.mouse.get_pos()
            if x_pos_mouse - size_width_pedal // 2 >= 0 and x_pos_mouse + size_width_pedal // 2 <= size_width_bg:
                x_pos_pedal = x_pos_mouse - size_width_pedal // 2
                rect_pedal.left = x_pos_mouse - size_width_pedal // 2

    # 배경 그리기
    background.fill('black')  # (255, 255, 255)

    # 페달 그리기
    pygame.draw.rect(background, (255, 255, 0), rect_pedal)

    # 공 좌표 계산
    if x_pos_ball - radius_ball <= 0:
        x_speed_ball = -x_speed_ball
    elif x_pos_ball >= size_width_bg - radius_ball:
        x_speed_ball = -x_speed_ball

    if y_pos_ball - radius_ball <= 0:
        y_speed_ball = -y_speed_ball
    elif y_pos_ball >= size_height_bg - radius_ball:  # 바닥 -> 나중에 게임오버로 변경
        y_speed_ball = -y_speed_ball                        #추후 해당 라인을 지우고 바닥에 닿으면 게임오버가 되도록 수정할것

    # 공 좌표에 스피드값 누적
    x_pos_ball += x_speed_ball
    y_pos_ball += y_speed_ball  

    # 공 그리기
    rect_ball.center = (x_pos_ball, y_pos_ball)     ##변경된 rect.center 값 저장
    pygame.draw.circle(background, (255, 0, 255), (x_pos_ball, y_pos_ball), size_radius_ball)

    ## 공 - 페달 닿았을 때
    if rect_ball.colliderect(rect_pedal):
        y_speed_ball = -y_speed_ball

    # 블록 그리기 (for문으로 10개*3층 만들기)
    for i in range(10):
        for j in range(3):
            if rect_block[i][j]:
                pygame.draw.rect(background, color_block[i][j], rect_block[i][j])
                rect_block[i][j].topleft = (i*size_width_block, j*size_height_block)

                ## 공 - 벽돌 닿았을 때
                if rect_ball.collidedict(rect_block[i][j]):
                    x_speed_ball = -x_speed_ball
                    y_speed_ball = -y_speed_ball
                    rect_block[i][j] = 0

    pygame.display.update()

pygame.quit()
