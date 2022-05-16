import sys, os
import pygame as pg

import games.gameList as inf
import common as c

gameNum = inf.gameNum
gamePerPage = inf.gamePerPage
pageNum = inf.pageNum

def gameSelectStart():
    state = 0   # 리턴용
    running = True
    while running:
        pg.display.set_caption("게임선택")
        gsDis = pg.display.set_mode(c.winSize)
        gsDis.fill(c.BLACK)

        # 게임 목록 페널 구성
        topMargin = 30
        gameListPanelWidth = 600
        gameListPanelHeight = 350

        gameListPanel = pg.draw.rect(gsDis, c.GRAY, ((c.winWidth - gameListPanelWidth) / 2, topMargin, 
                                                     gameListPanelWidth, gameListPanelHeight), 1)

        leftMargin = 15
        gameBoxWidth = 180
        gameBoxHeight = 120
        gameBox = []
        for i in range(gamePerPage):
            stand = int(((i * 2) % gamePerPage) / 2)
            if int((i * 2) / gamePerPage) % 2 == 0: # 게임 목록 중 첫번째 줄
                gameBox.append(pg.draw.rect(gsDis, c.GRAY, ((c.winWidth - gameListPanelWidth) / 2 + stand * gameBoxWidth + (stand + 1) * leftMargin, topMargin * 2, 
                                                            gameBoxWidth, gameBoxHeight), 1))
            else:                                   # 게임 목록 중 두번째 줄
                gameBox.append(pg.draw.rect(gsDis, c.GRAY, ((c.winWidth - gameListPanelWidth) / 2 + stand * gameBoxWidth + (stand + 1) * leftMargin, topMargin * 3 + 10 + gameBoxHeight, 
                                                            gameBoxWidth, gameBoxHeight), 1))

        # 버튼 구성
        btnWidth = 280
        btnHeight = 40
        playBtn = pg.draw.rect(gsDis, c.GRAY, (c.winWidth / 2 - btnWidth - 20, topMargin * 2+ gameListPanelHeight, 
                                               btnWidth, btnHeight), 1) # 게임시작
        backBtn = pg.draw.rect(gsDis, c.GRAY, (c.winWidth / 2 + 20, topMargin * 2 + gameListPanelHeight, 
                                               btnWidth, btnHeight), 1) # 뒤로가기

        focus = 0   # 게임 focus 선택된 게임 번호

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                state = 1
            # 클릭 이벤트
            elif event.type == pg.MOUSEBUTTONDOWN:
                if playBtn.collidepoint(event.pos):
                    pass
                elif backBtn.collidepoint(event.pos):
                    running = False

    return state
