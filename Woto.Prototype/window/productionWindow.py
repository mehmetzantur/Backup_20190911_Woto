from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from datetime import datetime

# Sabitler

piResolutionWidth = 800
piResolutionHeight = 480

heightHeader = 40
heightContent = 50
heightFooter = 50

fontSize20 = QFont()
fontSize20.setPointSize(20)


# Gönderilen nesneyi ekranda ortalar.
def centerWidget(widget):
    frameGm = widget.frameGeometry()
    screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
    centerPoint = QApplication.desktop().screenGeometry(screen).center()
    frameGm.moveCenter(centerPoint)
    widget.move(frameGm.topLeft())

class CQLineEdit(QLineEdit):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton: self.clicked.emit()
        else: super().mousePressEvent(event)

class ProductionWindow(QDialog):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowTitle('ÜRETİM')
        Form.setWindowFlag(Qt.WindowCloseButtonHint, False)
        Form.setWindowFlag(Qt.WindowFullscreenButtonHint, False)
        Form.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
        Form.setModal(True)
        centerWidget(Form)

        self.showDialogForAddOperatorHasLayout = False

        self.myDialog = QDialog()
        self.myDialog.setWindowTitle('OPERATÖR ve PROSES EKLE')
        self.myDialog.setModal(True)
        self.myDialog.setWindowFlag(Qt.WindowCloseButtonHint, False)
        centerWidget(self.myDialog)


        self.lblOperatorCode = QLabel('Sicil:')
        self.lblOperatorCode.setFont(fontSize20)

        self.lblProcessCode = QLabel('Proses:')
        self.lblProcessCode.setFont(fontSize20)


        self.focusedCQLineEdit = CQLineEdit()

        self.txtOperatorCode = CQLineEdit()
        self.txtOperatorCode.setObjectName('txtOperatorCode')
        self.txtOperatorCode.setFont(fontSize20)
        self.txtOperatorCode.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.txtOperatorCode.setPlaceholderText('1686')
        self.txtOperatorCode.clicked.connect(self.focusedLE)


        self.txtProcessCode = CQLineEdit()
        self.txtProcessCode.setObjectName('txtProcessCode')
        self.txtProcessCode.setFont(fontSize20)
        self.txtProcessCode.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.txtProcessCode.setPlaceholderText('1001')
        self.txtProcessCode.clicked.connect(self.focusedLE)

        self.numpadGrid = QGridLayout()
        self.inputGrid = QGridLayout()
        self.myDialogVBox = QVBoxLayout()

        self.inputGrid.addWidget(self.lblOperatorCode, 0, 0, 1, 2)
        self.inputGrid.addWidget(self.lblProcessCode, 0, 3, 1, 2)
        self.inputGrid.addWidget(self.txtOperatorCode, 1, 0, 1, 2)
        self.inputGrid.addWidget(self.txtProcessCode, 1, 3, 1, 2)
        self.myDialogVBox.addLayout(self.inputGrid)



        self.boxForm = QVBoxLayout(Form)


        # HEADER

        self.gridHeader = QGridLayout()
        self.gridHeader.setAlignment(Qt.AlignTop)

        self.lblWorkOrderNumber = QLabel('Emir:')
        self.lblWorkOrderNumber.setAlignment(Qt.AlignLeft)
        self.lblWorkOrderNumber.setFixedHeight(heightHeader)
        self.lblWorkOrderNumber.setFont(fontSize20)

        self.valWorkOrderNumber = QLabel('19-123')
        self.valWorkOrderNumber.setAlignment(Qt.AlignLeft)
        self.valWorkOrderNumber.setFixedHeight(heightHeader)
        self.valWorkOrderNumber.setFont(fontSize20)


        self.lblCounter = QLabel('Sağlam / Fire:')
        self.lblCounter.setAlignment(Qt.AlignVCenter)
        self.lblCounter.setAlignment(Qt.AlignHCenter)
        self.lblCounter.setFixedHeight(heightHeader)
        self.lblCounter.setFont(fontSize20)

        self.valCounter = QLabel('85 / 2')
        self.valCounter.setAlignment(Qt.AlignVCenter)
        self.valCounter.setAlignment(Qt.AlignHCenter)
        self.valCounter.setFixedHeight(heightHeader)
        self.valCounter.setFont(fontSize20)


        self.lblRegion = QLabel('Hücre:')
        self.lblRegion.setAlignment(Qt.AlignRight)
        self.lblRegion.setFixedHeight(heightHeader)
        self.lblRegion.setFont(fontSize20)

        self.valRegion = QLabel('A-03')
        self.valRegion.setAlignment(Qt.AlignRight)
        self.valRegion.setFixedHeight(heightHeader)
        self.valRegion.setFont(fontSize20)


        self.gridHeader.addWidget(self.lblWorkOrderNumber, 0, 0)
        self.gridHeader.addWidget(self.valWorkOrderNumber, 1, 0)

        self.gridHeader.addWidget(self.lblCounter, 0, 1)
        self.gridHeader.addWidget(self.valCounter, 1, 1)

        self.gridHeader.addWidget(self.lblRegion, 0, 2)
        self.gridHeader.addWidget(self.valRegion, 1, 2)

        self.lineH = QFrame(Form)
        self.lineH.setFrameShape(QFrame.HLine)
        self.lineH.setFrameShadow(QFrame.Sunken)
        self.gridHeader.addWidget(self.lineH, 2, 0, 1, 3)

        self.boxForm.addLayout(self.gridHeader)






        # CONTENT

        self.gridContent = QGridLayout()

        self.btnGrid = QPushButton('GRİD GELECEK')
        self.btnGrid.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #self.btnGrid.setFixedHeight(310)
        self.btnGrid.setFont(fontSize20)

        self.gridContent.addWidget(self.btnGrid, 1, 0, 1, 3)

        self.boxForm.addLayout(self.gridContent)



        # FOOTER

        self.gridFooter = QGridLayout()
        self.gridFooter.setAlignment(Qt.AlignBottom)

        self.lineB = QFrame(Form)
        self.lineB.setFrameShape(QFrame.HLine)
        self.lineB.setFrameShadow(QFrame.Sunken)

        self.btnClose = QPushButton('KAPAT')
        self.btnClose.clicked.connect(Form.reject)
        #self.btnClose.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btnClose.setFixedHeight(heightFooter)
        self.btnClose.setFont(fontSize20)

        self.btnStartStop = QPushButton('Başla')
        self.btnStartStop.setFixedHeight(heightFooter)
        self.btnStartStop.setFont(fontSize20)

        self.AddOperator = QPushButton('+ Operator')
        self.AddOperator.clicked.connect(self.btnClick_showDialogForAddOperator)
        self.AddOperator.setFixedHeight(heightFooter)
        self.AddOperator.setFont(fontSize20)

        self.gridFooter.addWidget(self.lineB, 0, 0, 1, 3)
        self.gridFooter.addWidget(self.btnClose, 1, 0)
        self.gridFooter.addWidget(self.btnStartStop, 1, 1)
        self.gridFooter.addWidget(self.AddOperator, 1, 2)

        self.boxForm.addLayout(self.gridFooter)



    def getNumpadGrid(self):
        txtNum = 1
        for i in range(3):
            for j in range(3):
                self.btnNumi = QPushButton()
                self.btnNumi.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.btnNumi.setText(str(txtNum))
                self.btnNumi.clicked.connect(self.btnClick_btnNumi)
                self.btnNumi.setFont(fontSize20)
                txtNum = txtNum + 1
                self.numpadGrid.addWidget(self.btnNumi, i, j)

        btnDel = QPushButton('SİL')
        btnDel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnDel.setFont(fontSize20)
        btnDel.clicked.connect(self.btnClick_btnDel)
        self.numpadGrid.addWidget(btnDel, 0, 3, 3, 1)

        btnClose = QPushButton('KAPAT')
        btnClose.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnClose.setFont(fontSize20)
        btnClose.clicked.connect(self.btnClick_btnClose)
        self.numpadGrid.addWidget(btnClose, 3, 0)


        btnNum0 = QPushButton('0')
        btnNum0.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnNum0.setFont(fontSize20)
        btnNum0.clicked.connect(self.btnClick_btnNumi)
        self.numpadGrid.addWidget(btnNum0, 3, 1)

        btnNext = QPushButton('DEVAM')
        btnNext.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnNext.setFont(fontSize20)
        btnNext.clicked.connect(self.btnClick_btnNext)
        self.numpadGrid.addWidget(btnNext, 3, 2, 1, 2)

        return self.numpadGrid


    def focusedLE(self):
        print(self.sender().objectName())
        self.focusedCQLineEdit = self.sender()

    def btnClick_showDialogForAddOperator(self):




        # textbox click eventine metot bağla bunu yaz. num btn lerin clicklerinde focusedWidget.settext yap
        #focusedWidget = QApplication.focusWidget()
        #print(focusedWidget.text())

        if self.showDialogForAddOperatorHasLayout == False:
            self.myDialogVBox.addLayout(self.getNumpadGrid())
            self.myDialog.setLayout(self.myDialogVBox)
            self.showDialogForAddOperatorHasLayout = True
        #self.myDialog.exec()
        self.myDialog.showFullScreen()


    def btnClick_btnClose(self):
        self.txtOperatorCode.setText('')
        self.txtProcessCode.setText('')
        self.myDialog.reject()

    def btnClick_btnNumi(self):
        btn = self.sender()
        self.focusedCQLineEdit.setText(self.focusedCQLineEdit.text() + btn.text())

    def btnClick_btnDel(self):
        self.focusedCQLineEdit.setText(self.focusedCQLineEdit.text()[:-1])

    def btnClick_btnNext(self):
        self.btnClick_btnClose()
        #self.productionWindow = QDialog()
        #self.ui = ProductionWindow()
        #self.ui.setupUi(self.productionWindow)
        #self.productionWindow.show()


def main():
    app = QApplication(sys.argv)
    mainWindow = ProductionWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


