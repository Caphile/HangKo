import pygame

pygame.init()  

backgraound = pygame.display.set_mode((500, 800))
pygame.display.set_caption("team13")

play = True
while play:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
pygame.quit()  
