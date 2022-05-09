import sys
import pygame as pg
#from pygame.locals import*

import common as c

def gameSelectStart():
    pg.init()

    pg.display.set_caption("test")
    gsDis = pg.display.set_mode(c.winSize)

    gsDis.fill(c.BLACK)

    running = True
    while running:
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False