import sys
import os
import pygame as pg

import common as c

def gameStart():

    pg.init()

    running = True
    while running:
        # 기본 틀
        pg.font.SysFont("notosanscjkkr", 10)
        pg.display.set_caption("Tetris")
        mainDis = pg.display.set_mode((720, 720))
        mainDis.fill((255, 255, 255))

        # 버튼 구성
        btnWidth = 350
        btnHeight = 28

        playBtn = pg.draw.rect(mainDis, c.GRAY, ((c.winWidth - btnWidth) / 2, c.winHeight / 2, 
                                                 btnWidth, btnHeight * 1.5), 1) # 게임시작
        
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
                elif exitBtn.collidepoint(event.pos):
                    running = False