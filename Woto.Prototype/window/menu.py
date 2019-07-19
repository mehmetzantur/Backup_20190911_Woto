# -*- coding: utf-8 -*-
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from controller.dbController import DbController
from window.production import Production




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

class Menu(QWidget):


    def __init__(self):
        super(Menu, self).__init__()

        DbController().initDb()

        self.setLayout(self._buildUI())
        # self.show()
        self.showFullScreen()


    def _buildUI(self):

        btnStartProduction = QPushButton('ÜRETİM BAŞLAT')
        btnStartProduction.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnStartProduction.clicked.connect(self.showProductionWindow)
        btnStartProduction.setFont(fontSize20)

        btnMenu2 = QPushButton('MENÜ2')
        btnMenu2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnMenu2.setFont(fontSize20)

        btnMenu3 = QPushButton('MENÜ3')
        btnMenu3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnMenu3.setFont(fontSize20)

        btnMenu4 = QPushButton('MENÜ4')
        btnMenu4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnMenu4.setFont(fontSize20)

        btnMenu5 = QPushButton('MENÜ5')
        btnMenu5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnMenu5.setFont(fontSize20)

        btnMenu6 = QPushButton('MENÜ6')
        btnMenu6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnMenu6.setFont(fontSize20)

        btnMenu7 = QPushButton('MENÜ7')
        btnMenu7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnMenu7.setFont(fontSize20)

        btnMenu8 = QPushButton('MENÜ8')
        btnMenu8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnMenu8.setFont(fontSize20)

        btnClose = QPushButton('KAPAT')
        btnClose.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnClose.clicked.connect(QCoreApplication.instance().quit)
        btnClose.setFont(fontSize20)

        menuGrid = QGridLayout()
        menuGrid.addWidget(btnStartProduction, 0, 0)
        menuGrid.addWidget(btnMenu2, 0, 1)
        menuGrid.addWidget(btnMenu3, 0, 2)
        menuGrid.addWidget(btnMenu4, 1, 0)
        menuGrid.addWidget(btnMenu5, 1, 1)
        menuGrid.addWidget(btnMenu6, 1, 2)
        menuGrid.addWidget(btnMenu7, 2, 0)
        menuGrid.addWidget(btnMenu8, 2, 1)
        menuGrid.addWidget(btnClose, 2, 2)

        return menuGrid


    def showProductionWindow(self):
        self.productionWindow = QWidget()
        self.productionWindowUI = Production()
        self.productionWindowUI._buildUI(self.productionWindow)



def main():
    app = QApplication(sys.argv)
    menu = Menu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



