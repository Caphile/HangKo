import sys
import pygame as pg

import common as c

def pauseStart(dis):
    # ��ư ����
    btnWidth = 350
    btnHeight = 28

    pausePanel = pg.draw.rect(dis, c.WHITE, (0, 0, c.winWidth, c.winHeight), 1)  # �Ͻ�����

    playBtn = pg.draw.rect(dis, c.GRAY, ((c.winWidth - btnWidth) / 2, c.winHeight / 2, 
                                                btnWidth, btnHeight * 1.5), 1) # ���ӽ���
    SetBtn = pg.draw.rect(dis, c.GRAY, ((c.winWidth - btnWidth) / 2, c.winHeight / 2 + btnHeight * 2, 
                                                btnWidth, btnHeight * 1.5), 1) # ��ŷ
    exitToMainBtn = pg.draw.rect(dis, c.GRAY, ((c.winWidth - btnWidth) / 2, c.winHeight / 2 + btnHeight * 4, 
                                            btnWidth, btnHeight * 1.5), 1) # ����
    exitToWinBtn = pg.draw.rect(dis, c.GRAY, ((c.winWidth - btnWidth) / 2, c.winHeight / 2 + btnHeight * 6, 
                                                btnWidth, btnHeight * 1.5), 1) # ����
    running = True
    while running:
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

