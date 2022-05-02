import sys
import pygame as pg
#from pygame.locals import*

pg.init()

disp = pg.display.set_mode((800, 600))
pg.display.set_caption("test")

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
