import pygame
import random

def gameStart():
    # 화면 크기 정보
    SCREEN_WIDTH = 720
    SCREEN_HEIGHT = 720

    # 파이게임 초기화 및 화면 크기 지정
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # 데이터 로드
    background_image = pygame.image.load('images/background.png')
    platform_image = pygame.image.load('images/platform.png')
    player_image = pygame.image.load('images/man.png')
    ddong_image = pygame.image.load('images/ddong.png')

    # 바닥 초기화
    platform_height = platform_image.get_size()[1]
    platform_pos_y = SCREEN_HEIGHT - platform_height

    # 플레이어 초기화
    player_width = player_image.get_size()[0]
    player_height = player_image.get_size()[1]
    player_pos_x = SCREEN_WIDTH / 2 - player_width / 2
    player_pos_y = SCREEN_HEIGHT - player_height - platform_height

    # 똥 초기화
    ddong_width = ddong_image.get_size()[0]
    ddong_height = ddong_image.get_size()[1]
    ddong_pos_x = random.randint(0, SCREEN_WIDTH - ddong_width+1)
    ddong_pos_y = -2*random.randint(ddong_height, 300)

    ddong_2_width = ddong_image.get_size()[0]
    ddong_2_height = ddong_image.get_size()[1]
    ddong_2_pos_x = random.randint(0, SCREEN_WIDTH - ddong_width+1)
    ddong_2_pos_y = -random.randint(ddong_height, 300)

    ddong_3_width = ddong_image.get_size()[0]
    ddong_3_height = ddong_image.get_size()[1]
    ddong_3_pos_x = random.randint(0, SCREEN_WIDTH - ddong_width+1)
    ddong_3_pos_y = -3*random.randint(ddong_height, 300)



    # 게임 루프를 제어하는 변수
    is_running = True

    # 시계 객체 생성
    clock = pygame.time.Clock()

    count = 0

    # 게임 루프 시작
    while is_running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        # 업데이트
        key = pygame.key.get_pressed()

        # 왼쪽 방향키 -> 왼쪽 이동
        if key[pygame.K_LEFT] == 1:
            player_pos_x -= 700 * clock.get_time() / 1000

        # 오른쪽 방향키 -> 오른쪽으로 이동
        if key[pygame.K_RIGHT] == 1:
            player_pos_x += 700 * clock.get_time() / 1000

        if player_pos_x < 0:
            player_pos_x = 0

        if player_pos_x > SCREEN_WIDTH - player_width:
            player_pos_x = SCREEN_WIDTH - player_width

        # 똥이 떨어지게 설정
        ddong_pos_y += 700 * clock.get_time() / 1000
        ddong_2_pos_y += 700 * clock.get_time() / 1000
        ddong_3_pos_y += 700 * clock.get_time() / 1000

        if ddong_pos_y > SCREEN_HEIGHT - platform_height - ddong_height:
            ddong_pos_x = random.randint(0, SCREEN_WIDTH - ddong_width + 1)
            ddong_pos_y = -2*random.randint(ddong_height, 500)

        if ddong_2_pos_y > SCREEN_HEIGHT - platform_height - ddong_2_height :
            ddong_2_pos_x = random.randint(0, SCREEN_WIDTH - ddong_2_width + 1)
            ddong_2_pos_y = -random.randint(ddong_2_height, 200)

        if ddong_3_pos_y > SCREEN_HEIGHT - platform_height - ddong_3_height :
            ddong_3_pos_x = random.randint(0, SCREEN_WIDTH - ddong_3_width + 1)
            ddong_3_pos_y = -3*random.randint(ddong_3_height, 200)

        # 각종 처리(충돌)
        player_rect = player_image.get_rect()
        player_rect.x = player_pos_x
        player_rect.y = player_pos_y

        ddong_rect = ddong_image.get_rect()
        ddong_2_rect = ddong_image.get_rect()
        ddong_3_rect = ddong_image.get_rect()

        ddong_2_rect.x = ddong_2_pos_x
        ddong_2_rect.y = ddong_2_pos_y
        ddong_rect.x = ddong_pos_x
        ddong_rect.y = ddong_pos_y
        ddong_3_rect.y = ddong_3_pos_y
        ddong_3_rect.x = ddong_3_pos_x

        # 충돌 검사
        if player_rect.colliderect(ddong_rect):
            print('충돌')
            is_running = False

        if player_rect.colliderect(ddong_2_rect):
            print('충돌')
            is_running = False

        if player_rect.colliderect(ddong_3_rect):
            print('충돌')
            is_running = False

        #랜더(그리기)
        screen.blit(background_image, (0, 0))
        screen.blit(player_image, (player_pos_x, player_pos_y))
        screen.blit(ddong_image, (ddong_pos_x, ddong_pos_y))
        screen.blit(ddong_image, (ddong_2_pos_x, ddong_2_pos_y))
        screen.blit(ddong_image, (ddong_3_pos_x, ddong_3_pos_y))

        # 디스플레이 업데이트
        pygame.display.update()
        count += 1
    pygame.quit()

gameStart()