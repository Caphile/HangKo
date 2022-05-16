import os, sys, glob

# # 게임 리스트 불러오기
games = []
currentPath = os.getcwd()
currentPath = os.path.join(currentPath, 'games')
dirList = os.listdir(currentPath)
for i in dirList:
    if not(i == '__pycache__' or i == 'gameList.py'):
        games.append(i)
gameNum = len(games)
gamePerPage = 6
pageNum = int(gameNum / gamePerPage)