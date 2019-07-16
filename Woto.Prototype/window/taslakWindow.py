# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

# Sabitler

piResolutionWidth = 800
piResolutionHeight = 480

fontSize20 = QFont()
fontSize20.setPointSize(20)





# Gönderilen nesneyi ekranda ortalar.
def centerWidget(widget):
    frameGm = widget.frameGeometry()
    screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
    centerPoint = QApplication.desktop().screenGeometry(screen).center()
    frameGm.moveCenter(centerPoint)
    widget.move(frameGm.topLeft())

class MainWindow(QMainWindow):


    def __init__(self):
        super(MainWindow, self).__init__()

        deneme = QPushButton('Deneme')


        self.showFullScreen()



def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



