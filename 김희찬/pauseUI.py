import sys
import pygame as pg

import common as c

def pauseStart(dis):
    # 버튼 구성
    btnWidth = 350
    btnHeight = 28

    pausePanel = pg.draw.rect(dis, c.WHITE, (0, 0, c.winWidth, c.winHeight), 1)  # 일시정지

    playBtn = pg.draw.rect(dis, c.GRAY, ((c.winWidth - btnWidth) / 2, c.winHeight / 2, 
                                                btnWidth, btnHeight * 1.5), 1) # 게임시작
    SetBtn = pg.draw.rect(dis, c.GRAY, ((c.winWidth - btnWidth) / 2, c.winHeight / 2 + btnHeight * 2, 
                                                btnWidth, btnHeight * 1.5), 1) # 랭킹
    exitToMainBtn = pg.draw.rect(dis, c.GRAY, ((c.winWidth - btnWidth) / 2, c.winHeight / 2 + btnHeight * 4, 
                                            btnWidth, btnHeight * 1.5), 1) # 설정
    exitToWinBtn = pg.draw.rect(dis, c.GRAY, ((c.winWidth - btnWidth) / 2, c.winHeight / 2 + btnHeight * 6, 
                                                btnWidth, btnHeight * 1.5), 1) # 종료
    running = True
    while running:
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

