# Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)

# Window Size
winWidth = 720
winHeight = 720
winSize = (winWidth, winHeight)

isPlay = False

import pygame, os

def backSound(path):
    soundPath = path
    soundPath = os.path.join(soundPath, 'background.mp3')

    global BS
    BS = pygame.mixer.Sound(soundPath)
    return BS

def clickSound(path):
    soundPath = path
    soundPath = os.path.join(soundPath, 'buttonClick.wav')
    CS = pygame.mixer.Sound(soundPath)
    return CS