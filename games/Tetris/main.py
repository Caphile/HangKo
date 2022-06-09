import sys, os
import pygame as pg
import random

# Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)      # 사각
GREEN = (0, 255, 0)     # z자
PINK = (255,192,203)    # ㄱ자
ORANGE = (255,165,0)    # 1자

WINSIZE = (720, 720)

currentPath = os.path.dirname(__file__)

def gameStart():

    pg.init()

    state = 0

    colors = [GRAY, BLACK, BLUE, GREEN, PINK, ORANGE]

    BGPath = os.path.dirname(__file__)
    BGPath = os.path.join(BGPath, 'background.jpg')

    

    global block
    global newBlock
    global newBlockColor
    global nextColor
    global creatable
    global score

    score = 0

    # 기본 틀
    pg.display.set_caption("Tetris")
    ttDis = pg.display.set_mode(WINSIZE)
    ttDis.fill(WHITE)

    clock = pg.time.Clock()
    clock.tick(60)

    backGround = pg.image.load(BGPath)
    backGround = pg.transform.scale(backGround, WINSIZE)
    ttDis.blit(backGround, (0, 0))

    blockSize = 30
    block_X = 12
    block_Y = 22
    
    gameBoardMargin = 25
    gameBoardWidth = blockSize * block_X + 10
    gameBoardHeight = blockSize * block_Y + 10
    gameBoard = pg.draw.rect(ttDis, WHITE, (gameBoardMargin, gameBoardMargin, gameBoardWidth, gameBoardHeight))

    firstBlock_X = gameBoardMargin + 5
    firstBlock_Y = gameBoardMargin + 5

    infMargin = 35
    infWidth = 200
    infHeight = 400
    infBack = pg.draw.rect(ttDis, BLACK, (gameBoardWidth + gameBoardMargin * 2 + infMargin, infMargin * 2, infWidth, infHeight))
    Inf = pg.draw.rect(ttDis, WHITE, (gameBoardWidth + gameBoardMargin * 2 + infMargin, infMargin * 2, infWidth, infHeight), 10)

    text_X = infMargin + gameBoardMargin * 2 + gameBoardWidth + infWidth / 2
    text_Y = infMargin * 2

    def makeInf():
        infBack = pg.draw.rect(ttDis, BLACK, (gameBoardWidth + gameBoardMargin * 2 + infMargin, infMargin * 2, infWidth, infHeight))
        Inf = pg.draw.rect(ttDis, WHITE, (gameBoardWidth + gameBoardMargin * 2 + infMargin, infMargin * 2, infWidth, infHeight), 10)

        infFont = pg.font.SysFont("malgungothic", 28)
        blockInfText = infFont.render("다음 블록", True, WHITE)
        blockInfRect = blockInfText.get_rect()
        blockInfRect.center = (text_X, text_Y + 50)
        ttDis.blit(blockInfText, blockInfRect)

        scoreFont = pg.font.SysFont("malgungothic", 24)
        scoreText = scoreFont.render(str(score), True, WHITE)
        scoreRect = scoreText.get_rect()
        scoreRect.center = (text_X, text_Y + 300)
        ttDis.blit(scoreText, scoreRect)

        scoreInfText = infFont.render("점수", True, WHITE)
        scoreInfRect = scoreInfText.get_rect()
        scoreInfRect.center = (text_X, text_Y + 230)
        ttDis.blit(scoreInfText, scoreInfRect)

        pg.display.update()

    isEnd = True
    running = True
    creatable = True
    while running:
        for i in range(block_Y):
            for j in range(block_X):
                pg.draw.rect(ttDis, GRAY, (firstBlock_X + j * blockSize, firstBlock_Y + i * blockSize, blockSize, blockSize))
                pg.draw.rect(ttDis, BLACK, (firstBlock_X + j * blockSize, firstBlock_Y + i * blockSize, blockSize, blockSize), 1)

        btnWidth = 180
        btnHeight = 70

        myFont = pg.font.SysFont("malgungothic", 28)

        playBtn = pg.draw.rect(ttDis, GRAY, (text_X - btnWidth / 2, text_Y + infHeight + infMargin, btnWidth, btnHeight)) # 게임시작
        playBtnText = myFont.render("시작", True, BLACK)
        playTextRect = playBtnText.get_rect()
        playTextRect.center = (text_X, text_Y + infHeight + infMargin + btnHeight / 2)
        ttDis.blit(playBtnText, playTextRect)

        exitBtn = pg.draw.rect(ttDis, GRAY, (text_X - btnWidth / 2, text_Y + infHeight + infMargin + 90, btnWidth, btnHeight)) # 종료
        exitBtnText = myFont.render("종료", True, BLACK)
        exitTextRect = exitBtnText.get_rect()
        exitTextRect.center = (text_X, text_Y + infHeight + infMargin + btnHeight / 2 + 90)
        ttDis.blit(exitBtnText, exitTextRect)

        makeInf()

        nextColor = random.randrange(2, 6)
        while not isEnd:
            if creatable == True:
                clearCount = 0 
                for line in range(1, block_Y - 1):      # 점수 획득
                    fullChk = True
                    for i in range(1, block_X - 1):
                        if block[i][line] == 1:
                            fullChk = False
                            break
                    if fullChk == True:
                        scoreSoundPath = os.path.join(currentPath, 'scoreSound.mp3')
                        pg.mixer.music.load(scoreSoundPath)
                        pg.mixer.music.play()
                        for i in range(1, block_X - 1):
                            for j in range(line, 1, -1):
                                block[i][j] = block[i][j - 1]
                            block[i][1] = 1
                        clearCount += 1

                score += int(clearCount * (clearCount + 1) / 2)
                makeInf()

                for i in range(1, block_X - 1): # 게임 오버
                    if block[i][1] != 1:
                        isEnd = True
                        break
                if isEnd == True:
                    gameOverSoundPath = os.path.join(os.path.abspath(os.path.join(currentPath, os.pardir)), 'end.mp3')
                    GOS = pg.mixer.Sound(gameOverSoundPath)
                    GOS.set_volume(0.2)
                    GOS.play()
                    break

                newBlockColor = nextColor
                nextColor = random.randrange(2, 6)
                X = int(block_X / 2)                                    # 새 블록
                if newBlockColor == 2:
                    newBlock = [(X - 1, 1), (X, 1), (X - 1, 2), (X, 2)]
                elif newBlockColor == 3:
                    newBlock = [(X - 1, 1), (X, 1), (X, 2), (X + 1, 2)]
                elif newBlockColor == 4:
                    newBlock = [(X - 1, 1), (X, 1), (X + 1, 1), (X + 1, 2)]
                elif newBlockColor == 5:
                    newBlock = [(X - 1, 1), (X, 1), (X + 1, 1), (X + 2, 1)]

                for (x, y) in newBlock:
                    block[x][y] = newBlockColor
                creatable = False

                nextBlock = [[0 for _ in range(4)] for _ in range(4)]   # 다음 블록
                X = 1
                if nextColor == 2:
                    nextNewBlock = [(X, 1), (X + 1, 1), (X, 2), (X + 1, 2)]
                elif nextColor == 3:
                    nextNewBlock = [(X - 1, 1), (X, 1), (X, 2), (X + 1, 2)]
                elif nextColor == 4:
                    nextNewBlock = [(X - 1, 1), (X, 1), (X + 1, 1), (X + 1, 2)]
                elif nextColor == 5:
                    nextNewBlock = [(X - 1, 1), (X, 1), (X + 1, 1), (X + 2, 1)]

                infBlock_X = text_X - infMargin - 25
                infBlock_Y = text_Y + infMargin * 2
                for (x, y) in nextNewBlock:
                    nextBlock[x][y] = nextColor

                for i in range(4):
                    for j in range(4):
                        color = nextBlock[j][i]
                        if color != 0 and color != 1:
                            pg.draw.rect(ttDis, colors[color], (infBlock_X + j * blockSize, infBlock_Y + i * blockSize, blockSize, blockSize))
                            pg.draw.rect(ttDis, BLACK, (infBlock_X + j * blockSize, infBlock_Y + i * blockSize, blockSize, blockSize), 1)
                        else:
                            pg.draw.rect(ttDis, BLACK, (infBlock_X + j * blockSize, infBlock_Y + i * blockSize, blockSize, blockSize))

            elif creatable == False:
                moveDown(0, 1)
                pg.time.delay(400)

            for i in range(block_Y):
                for j in range(block_X):
                    color = block[j][i]
                    pg.draw.rect(ttDis, colors[color], (firstBlock_X + j * blockSize, firstBlock_Y + i * blockSize, blockSize, blockSize))
                    pg.draw.rect(ttDis, BLACK, (firstBlock_X + j * blockSize, firstBlock_Y + i * blockSize, blockSize, blockSize), 1)
        
            pg.display.update()   # 화면 갱신

            for event in pg.event.get():
                # 프로그램 종료
                if event.type == pg.QUIT:
                    running = False
                    isEnd = True
                    state = 1
                # 키보드 이벤트
                elif event.type == pg.KEYDOWN:
                    blockSoundPath = os.path.join(currentPath, 'blockSound.mp3')
                    pg.mixer.music.load(blockSoundPath)
                    if event.key == pg.K_LEFT:
                        pg.mixer.music.play()
                        move(-1, 0)
                    elif event.key == pg.K_RIGHT:
                        pg.mixer.music.play()
                        move(1, 0)
                    elif event.key == pg.K_DOWN:    # 아래 방향키, 소프트 드랍
                        pg.mixer.music.play()
                        moveDown(0, 1)
                    elif event.key == pg.K_SPACE:   # 스페이스, 하드 드랍
                        pg.mixer.music.play()
                        while creatable == False:
                            moveDown(0, 1)
                    elif event.key == pg.K_z:   # z키, 시계 회전
                        pg.mixer.music.play()
                        turn(1)
                    elif event.key == pg.K_x:   # x키, 뒤집기
                        pg.mixer.music.play()
                        rvs()
                elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    if exitBtn.collidepoint(event.pos):
                        isEnd = True
                        running = False

#------------------------------------------------------------------------

        for event in pg.event.get():
            # 프로그램 종료
            if event.type == pg.QUIT:
                running = False
                state = 1
            # 클릭 이벤트
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:

                clickSoundPath = os.path.join(os.path.abspath(os.path.join(currentPath, os.pardir, os.pardir)), 'buttonClick.wav')
                BCS = pg.mixer.Sound(clickSoundPath)

                if playBtn.collidepoint(event.pos):

                    BCS.play()

                    score = 0
                    isEnd = False
                    block = [[1 for _ in range(block_Y)] for _ in range(block_X)]   # 0 GRAY, 1 BLACK, 2 BLUE, 3 GREEN, 4 PINK, 5 ORAGNE
                    for i in range(block_X):
                        block[i][0] = 0
                        block[i][block_Y - 1] = 0
                    for i in range(block_Y):
                        block[0][i] = 0
                        block[block_X - 1][i] = 0
                elif exitBtn.collidepoint(event.pos):

                    BCS.play()

                    running = False
                    isEnd = True

    saveRecord(loadRecord(), score)
    return state

def moveDown(tx, ty):
    global creatable
    for (x, y) in newBlock:
        blockColor = block[x][y]
        if block[x][y + 1] != 1 and (x + tx, y + ty) not in newBlock:
            creatable = True
            break

    if creatable == False:
        for (x, y) in newBlock:
            block[x][y] = 1
        for i, (x, y) in enumerate(newBlock):
            block[x + tx][y + ty] = newBlockColor
            newBlock[i] = (x + tx, y + ty)

def move(tx, ty):
    moveable = True
    for (x, y) in newBlock:
        blockColor = block[x][y]
        if block[x + tx][y + ty] != 1 and (x + tx, y + ty) not in newBlock:
            moveable = False
            break

    if moveable == True:
        for (x, y) in newBlock:
            block[x][y] = 1
        for i, (x, y) in enumerate(newBlock):
            block[x + tx][y + ty] = newBlockColor
            newBlock[i] = (x + tx, y + ty)

    pg.display.update()

def turn(dir):  # dir : -1 반시계, 1 시계        반시계 오류로 잠정 제외
    if newBlockColor == 3 or newBlockColor == 4:    # z자, ㄱ자
        centerIdx = 1
        cx, cy = newBlock[centerIdx]
        for i in [0, 2, 3]:
            tx, ty = newBlock[i]
            block[tx][ty] = 1
            if cx == tx and cy + 1 == ty:
                tx -= dir
                ty -= 1
            elif cx == tx and cy - 1 == ty:
                tx += dir
                ty += 1
            elif cx + 1 == tx and cy == ty:
                tx -= dir
                ty += 1
            elif cx + 1 == tx and cy + 1 == ty:
                tx -= dir + 1
                ty += dir - 1
            elif cx + 1 == tx and cy - 1 == ty:
                tx += dir - 1
                ty += dir + 1
            elif cx - 1 == tx and cy == ty:
                tx += 1
                ty -= dir
            elif cx - 1 == tx and cy + 1 == ty:
                tx += dir - 1
                ty -= dir + 1
            elif cx - 1 == tx and cy - 1 == ty:
                tx += dir + 1
                ty -= dir - 1

            newBlock[i] = (tx, ty)

    elif newBlockColor == 5:    # 1자
        centerIdx = 2
        cx, cy = newBlock[centerIdx]
        tempIdx = 0
        tx, ty = newBlock[tempIdx]

        if cx != tx:    # 가로 -> 세로
            dir = 1
        else:
            dir = -1    # 세로 -> 가로

        for i in [0, 1, 3]:
            tx, ty = newBlock[i]
            block[tx][ty] = 1
            if dir == 1:
                tx = cx
                ty = cy + i - 2
            else:
                tx = cx + i - 2
                ty = cy

            newBlock[i] = (tx, ty)

    for (x, y) in newBlock:
        block[x][y] = newBlockColor
            
def rvs():
    if newBlockColor == 3:
        x1, y1 = newBlock[0]
        block[x1][y1] = 1
        x2, y2 = newBlock[3]
        block[x2][y2] = 1
        newBlock[0] = (x2, y1)
        newBlock[3] = (x1, y2)

    elif newBlockColor == 4:
        tx, ty = newBlock[3]
        block[tx][ty] = 1
        cx, cy = newBlock[1]    # 비교
       
        if cx < tx:    # 오른쪽 -> 왼쪽
            tx -= 2
        else:           # 왼쪽 -> 오른쪽
            tx += 2

        newBlock[3] = (tx, ty)

    for (x, y) in newBlock:
        block[x][y] = newBlockColor

#saveRecord(loadRecord(), score)
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