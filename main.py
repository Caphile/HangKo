import sys
import os
import pygame as pg
import common as c
import gameSelectUI

def initialize_display(current_path):
    pg.init()

    # 기본 틀 설정
    pg.display.set_caption("HangKo")
    main_dis = pg.display.set_mode(c.winSize)

    # 아이콘 설정
    icon_path = os.path.join(current_path, 'icon.png')
    icon = pg.image.load(icon_path)
    pg.display.set_icon(icon)

    # 배경 설정
    bg_path = os.path.join(current_path, 'background1.png')
    background = pg.image.load(bg_path).convert()  # 이미지를 미리 변환하여 성능을 향상시킵니다.
    background = pg.transform.scale(background, c.winSize)
    main_dis.blit(background, (0, 0))

    pg.display.flip()  # 초기화된 화면을 화면에 반영합니다.
    return main_dis, background

def draw_button(display, text, center_x, center_y, width, height, color, text_color, action=None):
    my_font = pg.font.SysFont("malgungothic", 36)

    button_rect = pg.draw.rect(display, color, (center_x - width / 2, center_y - height / 2, width, height))
    text_render = my_font.render(text, True, text_color)
    text_rect = text_render.get_rect(center=(center_x, center_y))
    display.blit(text_render, text_rect)

    if action is not None:
        if button_rect.collidepoint(pg.mouse.get_pos()):
            if pg.mouse.get_pressed()[0]:
                action()

def main_start():
    current_path = os.getcwd()
    running = True

    main_dis, background = initialize_display(current_path)

    # 버튼 구성
    btn_width = 350
    btn_height = 100
    play_btn_x = c.winWidth / 2
    play_btn_y = 220 + btn_height / 2
    gap = 30

    while running:
        if not c.isPlay:
            c.backSound(current_path).play(-1)
            c.isPlay = True

        # 화면 초기화
        main_dis.blit(background, (0, 0))

        draw_button(main_dis, "게임시작", play_btn_x, play_btn_y, btn_width, btn_height, c.GRAY, c.BLACK, gameSelectUI.gameSelectStart)
        draw_button(main_dis, "종료", play_btn_x, play_btn_y + btn_height + gap, btn_width, btn_height, c.GRAY, c.BLACK, sys.exit)

        pg.display.update()
        pg.time.Clock().tick(30)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

    pg.quit()

if __name__ == "__main__":
    main_start()
