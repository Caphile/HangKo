import pygame

white = (255, 255, 255)
pad_width = 680
pad_height = 480
background_width = 680

def back(background, x, y):
    global gamepad
    gamepad.blit(background, (x, y))

def bird(bird_x_pos, bird_y_pos):
    global gamepad, flyingbird
    gamepad.blit(flyingbird, (bird_x_pos, bird_y_pos))

def runGame():
    global gamepad, flyingbird, clock, background1, background2

    bird_x_pos = 200
    bird_y_pos = (pad_height / 2) - 30
    to_y = 0

    background1_x = 0
    background2_x = background_width

    run = False
    while not run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    to_y -= 5
            if event.type == pygame.KEYUP:
                #if event.key == pygame.K_SPACE:
                to_y += 5 
        bird_y_pos += to_y

        gamepad.fill(white)

        background1_x -= 2
        background2_x -= 2

        if background1_x == -background_width:
            background1_x == background_width
        
        if background2_x == -background_width:
            background2_x == background_width

        back(background1, background1_x, 0)
        back(background2, background2_x, 0)
        bird(bird_x_pos, bird_y_pos)
        pygame.display.update()
        clock.tick(60)


    pygame.quit()

def initGame():
    global gamepad, flyingbird, clock, background1, background2

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('Flying bird')
    flyingbird = pygame.image.load("C:\\Users\\buij3\\OneDrive\\바탕 화면\\pygame\\pygame_basic\\pygame_1_Galaga\\images\\main_bird.png")
    background1 = pygame.image.load("C:\\Users\\buij3\\OneDrive\\바탕 화면\\pygame\\pygame_basic\\pygame_1_Galaga\\images\\background.png")
    background2 = background1.copy()

    clock = pygame.time.Clock()
    runGame()
initGame()
