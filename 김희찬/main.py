import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

formClass = uic.loadUiType('.\\test.ui')[0]

class App(QMainWindow, formClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
            
app = QApplication(sys.argv)
main = App()
main.show()
app.exec_()
