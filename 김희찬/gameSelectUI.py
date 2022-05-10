import sys
import pygame as pg

import common as c
import mainUI

# 게임개수
# 추후에 폴더 개수를 읽어와서 처리
games = []  # tuple로 저장, (이름, 이미지, ..)
gameNum = 8
pageNum = int(gameNum / 6)

def gameSelectStart():
    pg.init()

    pg.display.set_caption("게임선택")
    gsDis = pg.display.set_mode(c.winSize)
    gsDis.fill(c.BLACK)

    # 게임 목록 페널 구성
    topMargin = 30
    gameListPanelWidth = 600
    gameListPanelHeight = 350

    gameListPanel = pg.draw.rect(gsDis, c.GRAY, ((c.winWidth - gameListPanelWidth) / 2, topMargin, 
                                             gameListPanelWidth, gameListPanelHeight), 1)


    # 버튼 구성
    btnWidth = 280
    btnHeight = 40

    playBtn = pg.draw.rect(gsDis, c.GRAY, (c.winWidth / 2 - btnWidth - 20, topMargin * 2+ gameListPanelHeight, 
                                             btnWidth, btnHeight), 1) # 게임시작
    backBtn = pg.draw.rect(gsDis, c.GRAY, (c.winWidth / 2 + 20, topMargin * 2 + gameListPanelHeight, 
                                             btnWidth, btnHeight), 1) # 뒤로가기

    running = True
    while running:
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            # 클릭 이벤트
            elif event.type == pg.MOUSEBUTTONDOWN:
                if backBtn.collidepoint(event.pos):
                    mainUI.mainStart()