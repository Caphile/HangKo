import os
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import test

currentPath = os.getcwd()
currentPath = os.path.join(currentPath, 'HangKo')

mainForm = uic.loadUiType(currentPath + '\\main.ui')[0]
gameSelectForm = uic.loadUiType(currentPath + '\\gameSelect.ui')[0]

class Main(QMainWindow, mainForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn)

    def btn(self):
        layout = gameSelectForm

        '''
        self.hide()
        self.gameSelect = gameSelect()
        self.gameSelect.exec()
        
        self.show()
        '''
        

class gameSelect(QDialog, QWidget, gameSelectForm):
    def __init__(self):
        super(gameSelect, self).__init__()
        self.show()
            
app = QApplication(sys.argv)
main = Main()
main.show()
app.exec_()
