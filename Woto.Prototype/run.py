# -*- coding: utf-8 -*-
import os, sys, inspect

from controller.dbController import DbController
from controller.utilController import Constant as cons

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


from window.menu import Menu

# Sabitler

piResolutionWidth = 800
piResolutionHeight = 480

fontSize20 = QFont()
fontSize20.setPointSize(20)







class Main(QMainWindow):


    def __init__(self):
        super(Main, self).__init__()
        logoUrl = cons.logo_nonbg

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        lay = QVBoxLayout(self.central_widget)

        label = QLabel(self)
        #label.setScaledContents(True)
        pixmap = QPixmap(logoUrl)
        label.setPixmap(pixmap)
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet('padding-top:50px')
        lay.addWidget(label)

        boxTitle = QVBoxLayout()

        title = QLabel('W O T O')
        title.setStyleSheet('color:white; font-size:50px;')
        title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        title.setAlignment(Qt.AlignCenter)
        boxTitle.addWidget(title)

        subtitle = QLabel('prototype v0.01')
        subtitle.setStyleSheet('color:white; font-size:20px; font-style:italic')
        subtitle.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        subtitle.setAlignment(Qt.AlignCenter)
        boxTitle.addWidget(subtitle)

        lay.addLayout(boxTitle)


        self.resize(piResolutionWidth, piResolutionHeight)
        self.setStyleSheet('background-color:' + cons.color_wgrBlue_hex)

        print(self.height())

        result = DbController().initDb()
        print(result)

        QTimer.singleShot(1000, self.showMenuWindow)

        #self.show()
        self.showFullScreen()




    def showMenuWindow(self):
        self.menuWindow = QWidget()
        self.menuWindowUI = Menu()
        self.menuWindowUI._buildUI(self.menuWindow)
        self.close()



def main():
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



