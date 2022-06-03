import sys, os
import pygame as pg

import games.gameList as inf
import common as c

def gameSelectStart():

    gameNum = inf.gameNum
    gamePerPage = inf.gamePerPage
    pageNum = inf.pageNum

    state = 0   # 0 뒤로가기, 1 프로그램 종료
    currentPage = 0 # 현재 게임 페이지, 초기값 0
    focus = 0   # 게임 focus 선택된 게임 번호, 초기값 0

    running = True
    while running:
        pg.display.set_caption("게임선택")
        gsDis = pg.display.set_mode(c.winSize)
        gsDis.fill(c.BLACK)

        # 게임 목록 페널 구성
        panelTopMargin = 25
        gameListPanelWidth = 560
        gameListPanelHeight = 560

        gameListPanel = pg.draw.rect(gsDis, c.GRAY, ((c.winWidth - gameListPanelWidth) / 2, panelTopMargin, 
                                                     gameListPanelWidth, gameListPanelHeight), 1)

        gameBoxWidth = 150
        gameBoxHeight = 150
        gameBoxLeftMargin = (gameListPanelWidth - (gamePerPage / 2) * gameBoxWidth) / (gamePerPage / 2 + 1)
        gameBoxTopMargin = (gameListPanelHeight - (gameBoxHeight * 2) - panelTopMargin) / 2
        gameBox = []
        gameName = []
        gameIcon = []
        gameScore = []
        for i in range(gamePerPage):
            idx = currentPage * gamePerPage + i
            if focus == idx:
                color = c.RED
            else:
                if len(inf.icon) <= idx:
                    color = c.GRAY
                else:
                    color = c.WHITE

            if gamePerPage / 2 > i:
                gameBox.append(pg.draw.rect(gsDis, color, ((c.winWidth - gameListPanelWidth) / 2 + gameBoxLeftMargin * (1 + i) + gameBoxWidth * i, panelTopMargin * 2, 
                                                            gameBoxWidth, gameBoxHeight), 1))
                if len(inf.icon) > idx:
                    gameName.append(inf.game[idx])
                    gameIcon.append(pg.transform.scale(pg.image.load(inf.icon[idx]), (gameBoxWidth - 10, gameBoxHeight - 10)))
                    gsDis.blit(gameIcon[idx], ((c.winWidth - gameListPanelWidth) / 2 + gameBoxLeftMargin * (1 + i) + gameBoxWidth * i + 5, panelTopMargin * 2 + 5))
            else:
                gameBox.append(pg.draw.rect(gsDis, color, ((c.winWidth - gameListPanelWidth) / 2 + gameBoxLeftMargin * (1 + i - gamePerPage / 2) + gameBoxWidth * (i - gamePerPage / 2), panelTopMargin * 2 + gameBoxHeight + gameBoxTopMargin, 
                                                            gameBoxWidth, gameBoxHeight), 1))
                if len(inf.icon) > idx:
                    gameName.append(inf.game[idx])
                    gameIcon.append(pg.transform.scale(pg.image.load(inf.icon[idx]), (gameBoxWidth - 10, gameBoxHeight - 10)))
                    gsDis.blit(gameIcon[idx], ((c.winWidth - gameListPanelWidth) / 2 + gameBoxLeftMargin * (1 + i - gamePerPage / 2) + gameBoxWidth * (i - gamePerPage / 2) + 5, panelTopMargin * 2 + gameBoxHeight + gameBoxTopMargin + 5))


        # 버튼 구성
        btnWidth = 280
        btnHeight = 60
        playBtn = pg.draw.rect(gsDis, c.GRAY, (c.winWidth / 2 - btnWidth - 20, panelTopMargin * 3 - 20 + gameListPanelHeight, 
                                               btnWidth, btnHeight), 1) # 게임시작
        backBtn = pg.draw.rect(gsDis, c.GRAY, (c.winWidth / 2 + 20, panelTopMargin * 3 - 20 + gameListPanelHeight, 
                                               btnWidth, btnHeight), 1) # 뒤로가기


        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                state = 1
            # 클릭 이벤트
            elif event.type == pg.MOUSEBUTTONDOWN:
                for i, box in enumerate(gameBox):
                    if box.collidepoint(event.pos):
                        if len(inf.icon) > i:
                            focus = i
                if playBtn.collidepoint(event.pos):
                    if inf.playSelectedGame(gameName[focus]) == 1:
                        state = 1
                        running = False
                elif backBtn.collidepoint(event.pos):
                    running = False

    return state