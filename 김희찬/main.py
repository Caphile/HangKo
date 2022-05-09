import sys
import os
import pygame as pg

import common as c
import gameSelect

currentPath = os.getcwd()
currentPath = os.path.join(currentPath, 'HangKo')

def mainStart():
    pg.init()

    # 기본 틀
    pg.display.set_caption("main")
    mainDis = pg.display.set_mode(c.winSize)
    mainDis.fill(c.WHITE)

    # 버튼 구성
    a = pg.draw.rect(mainDis, c.GRAY, (300, 20, 50, 50), 1)

    running = True
    while running:
        pg.display.flip()   # 화면 갱신
        for event in pg.event.get():
            # 프로그램 종료
            if event.type == pg.QUIT:
                running = False
            # 클릭 이벤트
            elif event.type == pg.MOUSEBUTTONDOWN:
                if a.collidepoint(event.pos):
                    gameSelect.gameSelectStart()

mainStart()
