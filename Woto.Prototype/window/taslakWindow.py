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


class ProductionWindow(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(piResolutionWidth, piResolutionHeight)
        centerWidget(Form)
        self.pushButton = QPushButton(Form)
        self.pushButton.setGeometry(QRect(130, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")

        Form.setWindowTitle('Foorrrmmm')
        self.pushButton.setText('btn')





def main():
    app = QApplication(sys.argv)
    mainWindow = ProductionWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


