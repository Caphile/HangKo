import os, sys, glob

import games.Tetris.main as Tet
import games.SnakeGame.main as snake
import games.FlappyBird.main as bird
import games.DdongPihagi.main as DD
import games.BrickBreaking.main as BB

# # 게임 정보 불러오기
def getInf():
    global game
    global icon
    global record

    game = []
    icon = []  # 아이콘 사진파일의 dir 저장
    record = [] # 기록이 저장된 파일의 dir 저장

    currentPath = os.getcwd()
    currentPath = os.path.join(currentPath, 'games')
    dirList = os.listdir(currentPath)

    for i in dirList:
        if not(i == '__pycache__' or i == 'gameList.py' or i == 'end.mp3'):
            game.append(i)
            icon.append(os.path.join(currentPath, i, 'icon.png'))

            try:
                file = open(os.path.join(currentPath, i, 'record.txt'), 'r')
                data = str(file.readline())
                if data != '':
                    record.append(data + ' 점')
                else:
                    record.append('기록없음')
                file.close()
            except:
                record.append('기록없음')

    global gameNum
    global gamePerPage
    global pageNum

    gameNum = len(game)
    gamePerPage = 6
    pageNum = int(gameNum / gamePerPage)

# 게임선택화면 0, 프로그램 종료 1 리턴
def playSelectedGame(name):
    if name == 'Tetris':
        return Tet.gameStart()
    elif name == 'SnakeGame':
        return snake.gameStart()
    elif name == 'FlappyBird':
        return bird.gameStart()
    elif name == 'DdongPihagi':
        return DD.gameStart()
    elif name == 'BrickBreaking':
        return BB.gameStart()