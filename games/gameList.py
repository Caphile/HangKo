import os, sys, glob

import games.Tetris.main as Tet
import games.snakeGame.main as snake
#import games.flappybird.main as bird
#import games.DDong.main as DD
import games.BrickBreaking.main as BB

# # 게임 리스트 불러오기

game = []
icon = []  # 아이콘 사진파일의 dir 저장
record = [] # 기록이 저장된 파일의 dir 저장
currentPath = os.getcwd()
currentPath = os.path.join(currentPath, 'games')
dirList = os.listdir(currentPath)

for i in dirList:
    if not(i == '__pycache__' or i == 'gameList.py'):
        game.append(i)
        icon.append(os.path.join(currentPath, i, 'icon.png'))

gameNum = len(game)
gamePerPage = 6
pageNum = int(gameNum / gamePerPage)

# 게임선택화면 0, 프로그램 종료 1 리턴
def playSelectedGame(name):
    if name == 'Tetris':
        return Tet.gameStart()
    elif name == 'snakeGame':
        return snake.gameStart()
    elif name == 'flappybird':
        return bird.gameStart()
    elif name == 'DDong':
        return DD.gameStart()
    elif name == 'BrickBreaking':
        return BB.gameStart()