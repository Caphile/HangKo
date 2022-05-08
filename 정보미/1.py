import pygame

pygame.init() 

#화면 크기 설정
screen_width 
screen_height 
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Galaga") 

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\buij3\\OneDrive\\바탕 화면\\pygame\\pygame_basic\\pygame_1_Galaga\\galaga_background.png")


# 이벤트 루프
running = True # 게임이 진행중인가?/ 프로그램이 종료되지 않도록
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    screen.blit(background, (0, 0)) 
    pygame.display.update() 

# pygame 종료
pygame.quit()

