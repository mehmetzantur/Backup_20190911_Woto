# -*- coding: utf-8 -*-
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from controller.utilController import UtilController as util, Constant as const, WMenuButton, WLed, WHeader
from window.production import Production




# Gönderilen nesneyi ekranda ortalar.
def centerWidget(widget):
    frameGm = widget.frameGeometry()
    screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
    centerPoint = QApplication.desktop().screenGeometry(screen).center()
    frameGm.moveCenter(centerPoint)
    widget.move(frameGm.topLeft())



class Menu(QWidget):


    def _buildUI(self, Window):

        self.resize(const.piResolutionWidth, const.piResolutionHeight)
        oImage = QImage(const.bg_main_blur)
        sImage = oImage.scaled(QSize(const.piResolutionWidth, const.piResolutionHeight))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        #self.label = QLabel('Test', self)  # test, if it's really backgroundimage
        #self.label.setGeometry(50, 50, 200, 50)
        #css = "background-color:" + const.color_wgrBlue
        css = "background-image: url(asset/img/bg/mainbg.png)"
        #self.setStyleSheet(css)
        self.setLayout(self._buildMain())

        self.show()
        #self.showFullScreen()


    def _buildMain(self):
        boxRoot = QVBoxLayout()
        boxRoot.setContentsMargins(0, 0, 0, 0)

        widgetHeader = QWidget()
        widgetHeader.setFixedHeight(const.widgetHeaderHeight)
        widgetHeader.setStyleSheet("background-color: " + const.color_wgrBlue_hex)

        boxHeader = WHeader('WOTO', const.region)

        widgetHeader.setLayout(boxHeader)

        boxRoot.addWidget(widgetHeader)


        btnStartProduction = WMenuButton('ÜRETİM BAŞLAT', const.menu_icon_production)
        btnStartProduction.clicked.connect(self.showProductionWindow)

        btnMenu2 = WMenuButton('MENÜ2', const.menu_icon_star)

        btnMenu3 = WMenuButton('MENÜ3', const.menu_icon_star)

        btnMenu4 = WMenuButton('MENÜ4', const.menu_icon_star)

        btnMenu5 = WMenuButton('MENÜ5', const.menu_icon_star)

        btnMenu6 = WMenuButton('MENÜ6', const.menu_icon_star)

        btnMenu7 = WMenuButton('AYARLAR', const.menu_icon_settings)

        btnClose = WMenuButton('KAPAT', const.menu_icon_poweroff)
        btnClose.clicked.connect(QCoreApplication.instance().quit)

        gridMenu = QGridLayout()
        gridMenu.setContentsMargins(10, 5, 10, 5)
        gridMenu.addWidget(btnStartProduction, 0, 0)
        gridMenu.addWidget(btnMenu2, 0, 1)
        gridMenu.addWidget(btnMenu3, 0, 2)
        gridMenu.addWidget(btnMenu4, 0, 3)
        gridMenu.addWidget(btnMenu5, 1, 0)
        gridMenu.addWidget(btnMenu6, 1, 1)
        gridMenu.addWidget(btnMenu7, 1, 2)
        gridMenu.addWidget(btnClose, 1, 3)

        boxRoot.addLayout(gridMenu)

        widgetFooter = QWidget()
        widgetFooter.setFixedHeight(30)
        widgetFooter.setStyleSheet("background-color: " + const.color_wgrBlue_hex)

        boxFooter = QHBoxLayout()

        labelLeft = QLabel(const.version)
        labelLeft.setFont(const.font_fontSize10)
        labelLeft.setStyleSheet("color: white;")
        labelLeft.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        boxFooter.addWidget(labelLeft)

        ledOk = WLed(const.color_success_hex)
        boxFooter.addWidget(ledOk)

        ledWarning = WLed(const.color_warning_hex)
        boxFooter.addWidget(ledWarning)

        ledError = WLed(const.color_error_hex)
        boxFooter.addWidget(ledError)

        ledOff = WLed(const.color_darkgray_hex)
        boxFooter.addWidget(ledOff)

        labelRight = QLabel('20:57')
        labelRight.setFont(const.font_fontSize10)
        labelRight.setStyleSheet("color: white;")
        labelRight.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        boxFooter.addWidget(labelRight)

        widgetFooter.setLayout(boxFooter)

        boxRoot.addWidget(widgetFooter)
        return boxRoot


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



