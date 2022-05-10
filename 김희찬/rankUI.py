import sys
import pygame as pg

import common as c

def rankStart():
    pg.init()

    pg.display.set_caption("순위")
    gsDis = pg.display.set_mode(c.winSize)
    gsDis.fill(c.BLACK)

    running = True
    while running:
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False