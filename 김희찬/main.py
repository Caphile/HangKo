import os
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

currentPath = os.getcwd()
currentPath = os.path.join(currentPath, 'HangKo', 'main.ui')
print(currentPath)

formClass = uic.loadUiType(currentPath)[0]

class App(QMainWindow, formClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
            
app = QApplication(sys.argv)
main = App()
main.show()
app.exec_()