import pygame
import random
import os

def gameStart():
  
    state = 0

    pygame.init()

    currentPath = os.path.dirname(__file__)
    hitSoundPath = os.path.join(currentPath, 'hitSound.mp3')
    pygame.mixer.music.load(hitSoundPath)

    background = pygame.display.set_mode((720, 720))
    pygame.display.set_caption("BRICK BREAKING")

    # 배경 사이즈
    size_w_bg = background.get_size()[0]
    size_h_bg = background.get_size()[1]

    # 패들 사이즈, 좌표, Rect(모든 좌표를 모아서 갖고 있는 변수)
    size_w_pad = 100
    size_h_ped = 15

    x_pos_ped = size_w_bg // 2 - size_w_pad // 2
    y_pos_ped = size_h_bg - size_h_ped

    rect_ped = pygame.Rect(x_pos_ped, y_pos_ped, size_w_pad, size_h_ped)

    # 패들 좌.우 움직이기
    to_x_ped = 0

    # 공의 사이즈, 좌표, Rect
    size_r_ball = 18

    x_pos_ball = size_w_bg // 2
    y_pos_ball = size_h_bg - size_h_ped - size_r_ball

    rect_ball = pygame.Rect(x_pos_ball, y_pos_ball, size_r_ball*2, size_r_ball*2)
    rect_ball.center = (x_pos_ball, y_pos_ball)

    # 공의 방향과 스피드
    x_speed_ball = 0.17     
    y_speed_ball = 0.17

    # 블록 사이즈, 좌표, Rect
    size_w_block = size_w_bg // 12  
    size_h_block = 45       

    x_pos_block = 0
    y_pos_block = 0

    rect_block = [[] for _ in range(12)]
    color_block = [[] for _ in range(12)]

    for i in range(12):
        for j in range(5):         
            rect_block[i].append(pygame.Rect(
                i*size_w_block, j*size_h_block, size_w_block, size_h_block))
            color_block[i].append((random.randrange(255), random.randrange(
                150, 255), random.randrange(150, 255)))          #컬러값 랜덤

    # 마우스 좌표
    x_pos_mouse, y_pos_mouse = 0, 0

    # 점수
    score = 0

    # 시작 변수
    start = True

    # 글자 색, 폰트
    def game_text(word):
        font = pygame.font.SysFont(None, 100)

        text = font.render(word, True, (63, 204, 255))

        size_w_text = text.get_rect().size[0]
        size_h_text = text.get_rect().size[1]

        x_pos_text = size_w_bg/2 - size_w_text/2
        y_pos_text = size_h_bg/2 - size_h_text/2

        background.blit(text, (x_pos_text, y_pos_text))

    # 점수 표기를 위한 변수
    st = pygame.font.SysFont(None, 35)


    play = True
    while play:

        # 시작 시간 지연
        if start:
            start = False
            for i in range(3, 0, -1):
                background.fill((232, 226, 203))
                game_text(str(i))
                pygame.display.update()
                pygame.time.delay(1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                state = 1

            # 마우스로 패들 움직이기
            if event.type == pygame.MOUSEMOTION:
                x_pos_mouse, y_pos_mouse = pygame.mouse.get_pos()
                if x_pos_mouse - size_w_pad // 2 >= 0 and x_pos_mouse + size_w_pad // 2 <= size_w_bg:
                    x_pos_ped = x_pos_mouse - size_w_pad // 2
                    rect_ped.left = x_pos_mouse - size_w_pad // 2

        # 배경 그리기
        background.fill((232, 226, 203))  # ((255, 255, 255))

        # 패들 그리기
        pygame.draw.rect(background, (246, 143, 70), rect_ped)

        # 공 좌표 계산
        if x_pos_ball-size_r_ball <= 0:
            x_speed_ball = -x_speed_ball
        elif x_pos_ball >= size_w_bg-size_r_ball:
            x_speed_ball = -x_speed_ball

        if y_pos_ball-size_r_ball <= 0:
            y_speed_ball = -y_speed_ball
        elif y_pos_ball >= size_h_bg-size_r_ball:

            # y_speed_ball = -y_speed_ball  # 추후 해당 라인을 지우고 바닥에 닿으면 게임오버가 되도록 수정할것
            # 이 라인부터 break까지 주석처리하면 땅에 닿아도 게임오버 안됨
            gameOverSoundPath = os.path.join(os.path.abspath(os.path.join(currentPath, os.pardir)), 'end.mp3')
            GOS = pygame.mixer.Sound(gameOverSoundPath)
            GOS.set_volume(0.2)
            GOS.play()

            pygame.time.delay(1000)

            background.fill((232, 226, 203))
            game_text("GAME OVER")
            pygame.display.update()
            pygame.time.delay(1000)
            break

        # 공 좌표에 스피드값 누적
        x_pos_ball += x_speed_ball
        y_pos_ball += y_speed_ball

        # 공 그리기
        rect_ball.center = (x_pos_ball, y_pos_ball)  # 변경된 rect.center 값 저장
        pygame.draw.circle(background, (142, 170, 255),
                           (x_pos_ball, y_pos_ball), size_r_ball)

        # 공 - 패들 닿았을 때
        if rect_ball.colliderect(rect_ped):
            y_speed_ball = -y_speed_ball
            pygame.mixer.music.play()

        # 블록 생성 (for문으로 12*5층 만들기)
        for i in range(12):
            for j in range(5):         
                if rect_block[i][j]:
                    pygame.draw.rect(
                        background, color_block[i][j], rect_block[i][j])
                    rect_block[i][j].topleft = (i*size_w_block, j*size_h_block)

                    # 공 - 벽돌 닿았을 때
                    if rect_ball.colliderect(rect_block[i][j]):  
                        x_speed_ball = -x_speed_ball
                        y_speed_ball = -y_speed_ball
                        rect_block[i][j] = 0
                        score += 10                                  # 벽돌 하나당 10점

                        pygame.mixer.music.play()

        # 게임 클리어
        if score == 300:
            background.fill((232, 226, 203))
            game_text("GAME CLEAR")
            pygame.display.update()
            pygame.time.delay(1000)
            play = False

        stext = st.render(str(score), True, (142, 170, 255))
        background.blit(stext, (12, 695))

        pygame.display.update()

    #최고기록
    saveRecord(loadRecord(), score)

    return state

def loadRecord():
    currentPath = os.path.dirname(__file__) # 현재 파일의 위치 반환
    file = open(os.path.join(currentPath, 'record.txt'), 'r')

    high = file.readline()

    file.close()

    return high

def saveRecord(high, record):   # record는 항상 int
    if high == '' or int(high) < int(record):
        currentPath = os.path.dirname(__file__) # 현재 파일의 위치 반환
        file = open(os.path.join(currentPath, 'record.txt'), 'w')

        file.write(str(record))

        file.close()