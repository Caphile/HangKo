import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")  # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/user/OneDrive/바탕 화면/pygame_basic/background.png")

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
  for event in pygame.event.get():  # 마우스나 무슨 사건이 들어오는지 체크
    if event.type == pygame.QUIT:  # 창의 나가기 버튼
      running = False  # 게임 진행중 아님

  # screen.fill((0, 0, 255))  # 배경색을 채우기
  
  screen.blit(background, (0,0))  # 배경 그리기
  
  pygame.display.update()  # 게임 화면을 다시 그리기!

# pygame 종료
pygame.quit()