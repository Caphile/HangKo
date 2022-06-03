import sys
import os
import pygame as pg

import common as c
import gameSelectUI

currentPath = os.getcwd()
# currentPath = os.path.join(currentPath, 'HangKo')

def mainStart():

    pg.init()

    running = True
    while running:
        # 기본 틀
        myFont = pg.font.SysFont("malgungothic", 36)
        pg.display.set_caption("HangKo")
        mainDis = pg.display.set_mode(c.winSize)

        iconPath = currentPath
        iconPath = os.path.join(iconPath, 'icon.png')
        icon = pg.image.load(iconPath)
        pg.display.set_icon(icon)

        BGPath = currentPath
        BGPath = os.path.join(BGPath, 'background1.png')
        backGround = pg.image.load(BGPath)
        backGround = pg.transform.scale(backGround, c.winSize)
        mainDis.blit(backGround, (0, 0))

        clock = pg.time.Clock()
        clock.tick(10)

        # 버튼 구성
        btnWidth = 350
        btnHeight = 100
        playBtn_X = c.winWidth / 2
        playBtn_Y = 220 + btnHeight / 2
        gap = 30

        playBtn = pg.draw.rect(mainDis, c.GRAY, (playBtn_X - btnWidth / 2, playBtn_Y - btnHeight / 2, 
                                                 btnWidth, btnHeight)) # 게임시작
        playBtnText = myFont.render("게임시작", True, c.BLACK)
        playTextRect = playBtnText.get_rect()
        playTextRect.center = (playBtn_X, playBtn_Y)
        mainDis.blit(playBtnText, playTextRect)

        exitBtn = pg.draw.rect(mainDis, c.GRAY, (playBtn_X - btnWidth / 2, playBtn_Y + btnHeight / 2 + gap, 
                                                 btnWidth, btnHeight)) # 종료
        playBtnText = myFont.render("종료", True, c.BLACK)
        playTextRect = playBtnText.get_rect()
        playTextRect.center = (playBtn_X, playBtn_Y + btnHeight + gap)
        mainDis.blit(playBtnText, playTextRect)


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

mainStart()
pg.quit()
