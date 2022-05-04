import pygame

pygame.init()

backgraound = pygame.display.set_mode((480, 360))  # 가로, 세로
pygame.display.set_caption("team13")

play = True
while play:  # 콘솔창이 계속 지속되도록 하기위해서 while문을 씀
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
pygame.quit()
