import sys
import os
import pygame as pg

import common as c
import gameSelectUI, rankUI, settingUI

currentPath = os.getcwd()
currentPath = os.path.join(currentPath, 'HangKo')

def mainStart():

    pg.init()

    # 기본 틀
    pg.font.SysFont("notosanscjkkr", 10)
    pg.display.set_caption("프로그램 이름(미정)")
    mainDis = pg.display.set_mode(c.winSize)
    mainDis.fill(c.WHITE)

        running = True
        while running:
            pg.display.update()   # 화면 갱신

            for event in pg.event.get():
                # 프로그램 종료
                if event.type == pg.QUIT:
                    running = False
                # 클릭 이벤트
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if playBtn.collidepoint(event.pos):
                        if gameSelectUI.gameSelectStart() == 1:
                            running = False
                    elif rankBtn.collidepoint(event.pos):
                        rankUI.rankStart()
                    elif setBtn.collidepoint(event.pos):
                        settingUI.setStart()
                    elif exitBtn.collidepoint(event.pos):
                        running = False

mainStart()
pg.quit()
