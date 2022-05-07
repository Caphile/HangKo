import sys
import pygame as pg
#from pygame.locals import*

def play():
    pg.init()

    pg.display.set_caption("test")
    screen = pg.display.set_mode((800, 600))

    screen.fill((255, 255, 0))
    pg.display.flip()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
