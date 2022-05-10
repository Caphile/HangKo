import sys
import pygame as pg

import common as c

def setStart():
    pg.display.set_caption("설정")
    gsDis = pg.display.set_mode(c.winSize)
    gsDis.fill(c.BLACK)

    exitBtn = pg.draw.rect(mainDis, c.GRAY, ((c.winWidth - btnWidth) / 2, c.winHeight / 2 + btnHeight * 6, 
                                             btnWidth, btnHeight * 1.5), 1) # 종료

    running = True
    while running:
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

