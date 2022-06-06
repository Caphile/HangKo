import pygame, sys, random
from pygame.math import Vector2


class SNAKE:
    def __init__(self): # 뱀의 초기값
        self.snake = [Vector2(18, 33),Vector2(18, 34),Vector2(18, 35)]
        self.moveDirection = Vector2(0,-1) # 뱀의 이동방향 설정
        self.newSnake = False
        
        self.h_up = pygame.image.load('C:\doit\Vscode\python_workspace\snakeGame\image\h_up.png')
        self.h_down = pygame.image.load('C:\doit\Vscode\python_workspace\snakeGame\image\h_down.png')
        self.h_right = pygame.image.load('C:\doit\Vscode\python_workspace\snakeGame\image\h_right.png')
        self.h_left  = pygame.image.load('C:\doit\Vscode\python_workspace\snakeGame\image\h_left.png')
        
    def makeSnake(self): 
        self.headDraw()
        
        for i,j in enumerate(self.snake):
            x = int(j.x * boardSize)
            y = int(j.y * boardSize)
            headRect = pygame.Rect(x,y,boardSize,boardSize)
            
            if i == 0:
                screen.blit(self.h,headRect)
            else:
                pygame.draw.rect(screen,(119,12,199),headRect)
    
    def headDraw(self):
        changeHead = self.snake[1] - self.snake[0] # 이동 방향에 따른 머리 이미지 변경
        if changeHead == Vector2(1,0): # 왼쪽으로 이동
            self.h = self.h_left
        elif changeHead == Vector2(-1,0): # 오른쪽으로 이동
            self.h = self.h_right
        elif changeHead == Vector2(0,1): # 위로 이동
            self.h = self.h_up
        elif changeHead == Vector2(0,-1): # 아래로 이동
            self.h = self.h_down
        
    def snakeMove(self):
        if self.newSnake == True:
            snake_place = self.snake[:]
            snake_place.insert(0, snake_place[0] + self.moveDirection ) # 이동방향에 부착
            self.snake = snake_place[:] #
            self.newSnake = False
        else:
            snake_place = self.snake[:-1] # snake의 마지막을 복사
            snake_place.insert(0, snake_place[0] + self.moveDirection ) # 이동방향에 부착
            self.snake = snake_place[:] #
    
    def makenewSnake(self):
        self.newSnake = True
        
class Apple:
    def __init__(self): 
        self.randomApple()
        
    def makeApple(self):
        appleRect = pygame.Rect(int(self.place.x * boardSize),int(self.place.y* boardSize), boardSize,boardSize)
        screen.blit(apple,appleRect)

    def randomApple(self):
        self.x = random.randint(0,boardPlace - 1)
        self.y = random.randint(0,boardPlace - 1)
        self.place = Vector2(self.x,self.y)
        
class game:
    def __init__(self):
        self.character = SNAKE()
        self.apple = Apple()
        
    def checkSys(self):
        self.character.snakeMove()
        self.snakeEat()
        self.snakeCollision()
    
    def snakeEat(self): # 뱀이 과일을 먹으면
        if self.apple.place == self.character.snake[0]:
            self.apple.randomApple() # 과일을 다시 생성
            self.character.makenewSnake() # 뱀의 길이를 1칸 늘림
    
    def drawAll(self):
        self.apple.makeApple()
        self.character.makeSnake()
        self.makeScore()
        
    def makeScore(self):
        text = str(len(self.character.snake) - 3)
        scoreText = font.render(text, True, (0,0,0,))
        textX = int(boardSize*boardPlace-65)
        textY = int(boardSize*boardPlace-650)
        textRect = scoreText.get_rect(center = (textX,textY))
        screen.blit(scoreText,textRect)
    
    def recordScore(self):
        record = str(len(self.character.snake) - 3) # 사과 먹을 때마다 +1
        fr=open('record.txt', 'r', encoding='UTF8') # 최고기록을 저장
        line = fr.readline()
        if line == '기록없음':
            fw=open('record.txt','w') # 기록을 저장
            fw.write(record)
            fw.close()
        elif int(line) < int(record): # 현재 기록이 최고기록을 넘으면
            fw=open('record.txt','w') # 기록을 저장
            fw.write(record)
            fw.close()
        fr.close()
        
    def snakeCollision(self): # 게임종료 조건
        if not 0 <= self.character.snake[0].x < boardPlace or not 0 <= self.character.snake[0].y < boardPlace:
            self.gameOver() # 뱀이 화면 끝에 닿으면 게임종료
        
        for i in self.character.snake[1:]: # 뱀의 머리와 몸통이
            if i == self.character.snake[0]: # 만나면 게임종료
                self.gameOver() 

        
    def gameOver(self):
        pygame.quit()
        sys.exit()

pygame.init()
boardSize = 20
boardPlace = 36

screen = pygame.display.set_mode((boardPlace * boardSize, boardPlace * boardSize))
apple = pygame.image.load('C:/doit/Vscode/python_workspace/snakeGame/image/apple.png')# 사과 그래픽 변경
clock = pygame.time.Clock()
font = pygame.font.SysFont("notosanscjkkr", 30)
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

game_play = game()

def gameStart():
    while True:
        dt = clock.tick(144)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                game_play.checkSys()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if game_play.character.moveDirection.y != 1: # 현재 이동 방향과 정반대의 방향으로 움직일 수 없다
                        game_play.character.moveDirection = Vector2(0,-1) # 이동 방향을 위로 변경
                if event.key == pygame.K_LEFT:
                    if game_play.character.moveDirection.x != 1:
                        game_play.character.moveDirection = Vector2(-1,0) # 이동 방향을 왼쪽으로 변경
                if event.key == pygame.K_DOWN: 
                    if game_play.character.moveDirection.y != -1:
                        game_play.character.moveDirection = Vector2(0,1) # 이동 방향을 아래로 변경
                if event.key == pygame.K_RIGHT: 
                    if game_play.character.moveDirection.x != -1:
                        game_play.character.moveDirection = Vector2(1,0) # 이동 방향을 위로 변경
        
        game_play.recordScore()
        screen.fill((100, 100, 100))
        game_play.drawAll()
        pygame.display.update()

    pygame.quit()
