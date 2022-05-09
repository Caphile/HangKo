import sys
import os
import pygame as pg

import common as c
import gameSelect, rank, setting

currentPath = os.getcwd()
currentPath = os.path.join(currentPath, 'HangKo')

def mainStart():
    pg.init()

    # 기본 틀
    pg.font.SysFont("notosanscjkkr", 10)
    pg.display.set_caption("프로그램 이름(미정)")
    mainDis = pg.display.set_mode(c.winSize)
    mainDis.fill(c.WHITE)

    # 버튼 구성
    playBtn = pg.draw.rect(mainDis, c.GRAY, (300, 20, 50, 50), 1) # 게임시작
    rankBtn = pg.draw.rect(mainDis, c.GRAY, (300, 70, 50, 50), 1) # 랭킹
    setBtn = pg.draw.rect(mainDis, c.GRAY, (300, 120, 50, 50), 1) # 설정
    exitBtn = pg.draw.rect(mainDis, c.GRAY, (300, 170, 50, 50), 1) # 종료

    running = True
    while running:
        pg.display.flip()   # 화면 갱신
        for event in pg.event.get():
            # 프로그램 종료
            if event.type == pg.QUIT:
                running = False
            # 클릭 이벤트
            elif event.type == pg.MOUSEBUTTONDOWN:
                if playBtn.collidepoint(event.pos):
                    gameSelect.gameSelectStart()
                elif rankBtn.collidepoint(event.pos):
                    rank.rankStart()
                elif setBtn.collidepoint(event.pos):
                    setting.setStart()
                elif exitBtn.collidepoint(event.pos):
                    running = False

mainStart()
pg.quit()