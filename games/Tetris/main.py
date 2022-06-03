import sys
import os
import pygame as pg

import common as c


def gameStart():

    state = 0

    running = True
    while running:
        # 기본 틀
        pg.font.SysFont("notosanscjkkr", 10)
        pg.display.set_caption("Tetris")
        mainDis = pg.display.set_mode((720, 720))
        mainDis.fill((255, 255, 255))

        pg.display.update()   # 화면 갱신

        for event in pg.event.get():
            # 프로그램 종료
            if event.type == pg.QUIT:
                running = False
                state = 1
            # 키보드 이벤트
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    pass
                elif event.key == pg.K_RIGHT:
                    pass
                elif event.key == pg.K_DOWN:    # 아래 방향키, 소프트 드랍
                    pass
                elif event.key == pg.K-SPACE:   # 스페이스, 하드 드랍
                    pass
                elif event.key == pg.K-z:   # z키, 반 시계 회전
                    pass
                elif event.key == pg.K-x:   # x키, 시계 회전
                    pass

    return state

