# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

import RPi.GPIO as GPIO
import time


class MainWindow(QMainWindow):


    def __init__(self):
        super(MainWindow, self).__init__()

        self.setFixedSize(800, 430)


        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        root = QHBoxLayout(self.central_widget)

        btnPulse = QPushButton('PULSE')
        btnPulse.clicked.connect(self.generatePulse)
        btnPulse.setFixedHeight(400)
        root.addWidget(btnPulse)

        btnClose = QPushButton('KAPAT')
        btnClose.clicked.connect(self.btnClick_btnClose)
        btnClose.setFixedHeight(400)
        root.addWidget(btnClose)

        self.setLayout(root)
        self.show()


    def btnClick_btnClose(self):

        GPIO.cleanup()
        QCoreApplication.instance().quit()



    pin = 11
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)

    def generatePulse(self):

        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(1)

        GPIO.output(self.pin, GPIO.LOW)
        time.sleep(1)
        return

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



