import pygame         #45줄 오류 - TypeError: 'module' object is not callable
import random

pygame.init()   

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("벽돌 부수기")   

# 배경 사이즈
size_width_bg = background.get_size()[0]  # 0번 칸은 가로   
size_height_bg = background.get_size()[1]  # 1번 칸은 세로

# 페달의 사이즈, 좌표, Rect
size_width_pedal = 100
size_height_pedal = 15

x_pos_pedal = size_width_bg//2 - size_width_pedal//2
y_pos_pedal = size_height_bg - size_height_pedal

rect_pedal = pygame.Rect(x_pos_pedal, y_pos_pedal,size_width_pedal, size_height_pedal)

# pygame.rect는 모듈
# 모듈은 호출 할수 없음
# Rect 객체는 pygame.rect 모듈에 있음
# 따라서 pygame.rect.Rect(a, b, c, d)가 옳음
# 위의 경우 rect_pedal = pygame.rect.Rect(x_pos_pedal, y_pos_pedal,size_width_pedal, size_height_pedal)

# 공 사이즈, 좌표, Rect
size_radius_ball = 20

x_pos_ball = size_width_bg // 2
y_pos_ball = size_height_bg - size_height_pedal - size_radius_ball

rect_ball = pygame.Rect(x_pos_ball, y_pos_ball,                                   # 오류: 줄 밀림? 줄 분리?현상 __ 28줄 하나로 이어져야하는데 29줄로 넘어가버림
                        size_radius_ball*2, size_radius_ball*2)
rect_ball.center = (x_pos_ball, y_pos_ball)

# 블록 사이즈, 좌표, Rect  
size_width_block = size_width_bg // 10    
size_height_block = 30  
 
x_pos_block = 0  
y_pos_block = 0  

rect_block = [[] for _ in range(10)]
color_block = [[] for _ in range(10)]

for i in range(10):
    for j in range(3):
        rect_block[i].append(pygame.rect(                                         # (28줄과 동일)오류: 줄 밀림? 줄 분리?현상 __ 44줄 하나로 이어져야하는데 45줄로 넘어가버림
          i*size_width_block, j*size_height_block, size_height_block))
        color_block[i].append((random.randrange(255), random.randrange(           # (44줄과 동일)오류:
            150, 255), random.randrange(150, 255)))

play = True   #콘솔창 실행
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    # 배경색
    background.fill((255, 255, 255))

    # 페달 그리기   
    pygame.draw.rect(background, (255, 255, 0), rect_pedal)  

    # 공 그리기
    pygame.draw.circle(background,(255, 0, 255),(x_pos_ball,y_pos_ball),size_radius_ball)

    # 블록 그리기(for문으로 10*3)
    for i in range(10):
        for j in range(3):
            if rect_block[i][j]:
                pygame.draw.rect(background, color_block[i][j], rect_block[i][j])
                rect_block[i][j].topleft = (i*size_width_block, j*size_height_block)

    pygame.display.update()

pygame.quit()  
