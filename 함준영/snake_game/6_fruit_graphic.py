import pygame, sys, random
from pygame.math import Vector2


class SNAKE:
    def __init__(self): # 뱀의 초기값
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0) # 뱀의 이동방향 설정
        self.new_block = False
        
    def draw_snake(self): 
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,(183,111,122),block_rect)
    
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction ) # 이동방향에 부착
            self.body = body_copy[:] #
            self.new_block = False
        else:
            body_copy = self.body[:-1] # body의 마지막을 복사
            body_copy.insert(0, body_copy[0] + self.direction ) # 이동방향에 부착
            self.body = body_copy[:] #
    
    def add_block(self):
        self.new_block = True
class FRUIT:
    def __init__(self): 
        self.randomize()
        
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y* cell_size), cell_size,cell_size)
        screen.blit(apple,fruit_rect)
        # pygame.draw.rect(screen,(126,166,144),fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x,self.y)
        
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    
    def check_collision(self): # 뱀이 과일을 먹으면
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize() # 과일을 다시 생성
            self.snake.add_block() # 뱀의 길이를 1칸 늘림
    
    def check_fail(self): # 게임종료 조건
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over() # 뱀이 화면 끝에 닿으면 게임종료
        
        for block in self.snake.body[1:]: # 뱀의 머리와 몸통이
            if block == self.snake.body[0]: # 만나면 게임종료
                self.game_over() 


    def game_over(self):
        pygame.quit()
        sys.exit()
        
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('C:/doit/Vscode/python_workspace/snake_game/image/apple.png').convert_alpha() # 사과 그래픽 변경

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()


while True:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1: # 현재 이동 방향과 정반대의 방향으로 움직일 수 없다
                    main_game.snake.direction = Vector2(0,-1) # 이동 방향을 위로 변경
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0) # 이동 방향을 왼쪽으로 변경
            if event.key == pygame.K_DOWN: 
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1) # 이동 방향을 아래로 변경
            if event.key == pygame.K_RIGHT: 
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0) # 이동 방향을 위로 변경
        
    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()

pygame.quit()