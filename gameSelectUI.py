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
        myFont = pg.font.SysFont("malgungothic", 30)
        gsDis = pg.display.set_mode(c.winSize)
        gsDis.fill(c.BLACK)

        BGPath = os.getcwd()
        BGPath = os.path.join(BGPath, 'background2.png')
        backGround = pg.image.load(BGPath)
        backGround = pg.transform.scale(backGround, c.winSize)
        gsDis.blit(backGround, (0, 0))

        clock = pg.time.Clock()
        clock.tick(10)

        # 게임 박스 구성
        gameBoxWidth = 180
        gameBoxHeight = 180
        boxMargin = 40
        gameBox_X = boxMargin + gameBoxWidth / 2
        gameBox_Y = boxMargin + gameBoxHeight / 2
        textHeight = 80

        # 게임 목록 페널 구성
        panelMargin = 30
        panelWidth = c.winWidth - panelMargin * 2
        panelHeight = boxMargin - panelMargin + gameBoxHeight * 2 + textHeight * 2
        gameListPanel = pg.draw.rect(gsDis, c.BLACK, (panelMargin, panelMargin, panelWidth, panelHeight), 1)

        gameBox = []
        gameName = []
        gameIcon = []
        gameScore = []

        nameFont = pg.font.SysFont("malgungothic", 24)
        recordFont = pg.font.SysFont("malgungothic", 18)

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
                gameBox.append(pg.draw.rect(gsDis, color, (gameBox_X - gameBoxWidth / 2 + (gameBoxWidth + boxMargin) * i + 10, gameBox_Y - gameBoxHeight / 2, 
                                                            gameBoxWidth, gameBoxHeight), 1))
                if len(inf.icon) > idx:
                    gameName.append(inf.game[idx])
                    gameIcon.append(pg.transform.scale(pg.image.load(inf.icon[idx]), (gameBoxWidth - 10, gameBoxHeight - 10)))
                    gsDis.blit(gameIcon[idx], (gameBox_X - gameBoxWidth / 2 + (gameBoxWidth + boxMargin) * i + 15, gameBox_Y - gameBoxHeight / 2 + 5))

                    name = nameFont.render(inf.game[i], True, c.BLACK)
                    nameRect = name.get_rect()
                    nameRect.center = (gameBox_X + (gameBoxWidth + boxMargin) * i + 10, gameBox_Y + gameBoxHeight / 2 + 15)
                    gsDis.blit(name, nameRect)

                    record = recordFont.render(inf.record[i], True, c.BLACK)
                    recordRect = record.get_rect()
                    recordRect.center = (gameBox_X + (gameBoxWidth + boxMargin) * i + 10, gameBox_Y + gameBoxHeight / 2 + 50)
                    gsDis.blit(record, recordRect)

            else:
                j = i - gamePerPage / 2
                gameBox.append(pg.draw.rect(gsDis, color, (gameBox_X - gameBoxWidth / 2 + (gameBoxWidth + boxMargin) * j + 10, gameBox_Y - gameBoxHeight / 2 + gameBoxHeight + textHeight, 
                                                            gameBoxWidth, gameBoxHeight), 1))
                if len(inf.icon) > idx:
                    gameName.append(inf.game[idx])
                    gameIcon.append(pg.transform.scale(pg.image.load(inf.icon[idx]), (gameBoxWidth - 10, gameBoxHeight - 10)))
                    gsDis.blit(gameIcon[idx], (gameBox_X - gameBoxWidth / 2 + (gameBoxWidth + boxMargin) * j + 15, gameBox_Y - gameBoxHeight / 2 + gameBoxHeight + textHeight + 5))

                    name = nameFont.render(inf.game[i], True, c.BLACK)
                    nameRect = name.get_rect()
                    nameRect.center = (gameBox_X + (gameBoxWidth + boxMargin) * j + 10, gameBox_Y + gameBoxHeight * 1.5 + textHeight + 15)
                    gsDis.blit(name, nameRect)

                    record = recordFont.render(inf.record[i], True, c.BLACK)
                    recordRect = record.get_rect()
                    recordRect.center = (gameBox_X + (gameBoxWidth + boxMargin) * j + 10, gameBox_Y + gameBoxHeight * 1.5 + textHeight + 50)
                    gsDis.blit(record, recordRect)
                   
        # 버튼 구성
        btnWidth = 300
        btnHeight = 60
        btnMargin = 20
        playBtn_X = (c.winWidth - btnWidth - btnMargin) / 2
        playBtn_Y = panelMargin + panelHeight + (c.winHeight - (panelMargin + panelHeight + btnHeight)) / 2 + btnHeight / 2
        backBtn_X =(c.winWidth + btnWidth + btnMargin) / 2
        backBtn_Y = playBtn_Y

        playBtn = pg.draw.rect(gsDis, c.GRAY, (playBtn_X - btnWidth / 2, playBtn_Y - btnHeight / 2,
                                               btnWidth, btnHeight)) # 게임시작
        playBtnText = myFont.render("게임시작", True, c.BLACK)
        playTextRect = playBtnText.get_rect()
        playTextRect.center = (playBtn_X, playBtn_Y)
        gsDis.blit(playBtnText, playTextRect)


        backBtn = pg.draw.rect(gsDis, c.GRAY, (backBtn_X - btnWidth / 2, backBtn_Y - btnHeight / 2, 
                                               btnWidth, btnHeight)) # 뒤로가기
        backBtnText = myFont.render("뒤로가기", True, c.BLACK)
        backTextRect = backBtnText.get_rect()
        backTextRect.center = (backBtn_X, backBtn_Y)
        gsDis.blit(backBtnText, backTextRect)

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