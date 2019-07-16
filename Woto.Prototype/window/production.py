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

heightHeader = 40
heightContent = 50
heightFooter = 50


class CQLineEdit(QLineEdit):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton: self.clicked.emit()
        else: super().mousePressEvent(event)




# Gönderilen nesneyi ekranda ortalar.
def centerWidget(widget):
    frameGm = widget.frameGeometry()
    screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
    centerPoint = QApplication.desktop().screenGeometry(screen).center()
    frameGm.moveCenter(centerPoint)
    widget.move(frameGm.topLeft())




class Production(QWidget):

    def _buildUI(self, Window):

        self.setLayout(self._buildMain())
        #self.show()
        self.showFullScreen()

        self._showDialogStep1()


    def _buildMain(self):

        boxRoot = QVBoxLayout()

        #region HEADER

        gridHeader = QGridLayout()
        gridHeader.setAlignment(Qt.AlignTop)

        lblWorkOrderNumber = QLabel('Emir:')
        lblWorkOrderNumber.setAlignment(Qt.AlignLeft)
        lblWorkOrderNumber.setFixedHeight(heightHeader)
        lblWorkOrderNumber.setFont(fontSize20)
        gridHeader.addWidget(lblWorkOrderNumber, 0, 0)

        self.valWorkOrderNumber = QLabel('19-123')
        self.valWorkOrderNumber.setAlignment(Qt.AlignLeft)
        self.valWorkOrderNumber.setFixedHeight(heightHeader)
        self.valWorkOrderNumber.setFont(fontSize20)
        gridHeader.addWidget(self.valWorkOrderNumber, 1, 0)

        lblCounter = QLabel('Sağlam / Fire:')
        lblCounter.setAlignment(Qt.AlignVCenter)
        lblCounter.setAlignment(Qt.AlignHCenter)
        lblCounter.setFixedHeight(heightHeader)
        lblCounter.setFont(fontSize20)
        gridHeader.addWidget(lblCounter, 0, 1)

        self.valCounter = QLabel('85 / 2')
        self.valCounter.setAlignment(Qt.AlignVCenter)
        self.valCounter.setAlignment(Qt.AlignHCenter)
        self.valCounter.setFixedHeight(heightHeader)
        self.valCounter.setFont(fontSize20)
        gridHeader.addWidget(self.valCounter, 1, 1)

        lblRegion = QLabel('Hücre:')
        lblRegion.setAlignment(Qt.AlignRight)
        lblRegion.setFixedHeight(heightHeader)
        lblRegion.setFont(fontSize20)
        gridHeader.addWidget(lblRegion, 0, 2)

        self.valRegion = QLabel('A-03')
        self.valRegion.setAlignment(Qt.AlignRight)
        self.valRegion.setFixedHeight(heightHeader)
        self.valRegion.setFont(fontSize20)
        gridHeader.addWidget(self.valRegion, 1, 2)

        lineH = QFrame()
        lineH.setFrameShape(QFrame.HLine)
        lineH.setFrameShadow(QFrame.Sunken)
        gridHeader.addWidget(lineH, 2, 0, 1, 3)

        boxRoot.addLayout(gridHeader)

        #endregion

        #region CONTENT

        gridContent = QGridLayout()

        self.btnGrid = QPushButton('GRİD GELECEK')
        self.btnGrid.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.btnGrid.setFixedHeight(310)
        self.btnGrid.setFont(fontSize20)
        gridContent.addWidget(self.btnGrid, 1, 0, 1, 3)

        boxRoot.addLayout(gridContent)

        #endregion

        #region FOOTER

        gridFooter = QGridLayout()
        gridFooter.setAlignment(Qt.AlignBottom)

        lineB = QFrame()
        lineB.setFrameShape(QFrame.HLine)
        lineB.setFrameShadow(QFrame.Sunken)
        gridFooter.addWidget(lineB, 0, 0, 1, 3)

        btnClose = QPushButton('KAPAT')
        btnClose.clicked.connect(self.btnClick_btnClose)
        # self.btnClose.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnClose.setFixedHeight(heightFooter)
        btnClose.setFont(fontSize20)
        gridFooter.addWidget(btnClose, 1, 0)

        btnStartStop = QPushButton('Başla')
        btnStartStop.setFixedHeight(heightFooter)
        btnStartStop.setFont(fontSize20)
        gridFooter.addWidget(btnStartStop, 1, 1)

        btnAddOperator = QPushButton('+ Operator')
        #btnAddOperator.clicked.connect(self.btnClick_showDialogForAddOperator)
        btnAddOperator.setFixedHeight(heightFooter)
        btnAddOperator.setFont(fontSize20)
        gridFooter.addWidget(btnAddOperator, 1, 2)

        boxRoot.addLayout(gridFooter)

        #endregion

        return boxRoot




    #region STEP DIALOGS

    def _showDialogStep1(self):

        self.focusedCQLineEdit = CQLineEdit()

        self.step1Dialog = QDialog()
        self.step1Dialog.setLayout(self._buildStep1())
        self.step1Dialog.setWindowTitle('Emir No giriniz...')
        # self.step1Dialog.setWindowFlag(Qt.FramelessWindowHint)
        # self.step1Dialog.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.step1Dialog.setWindowOpacity(0.9)
        self.step1Dialog.resize(600, 380)
        self.step1Dialog.exec()
        centerWidget(self.step1Dialog)

    def _showDialogStep2(self):

        self.focusedCQLineEdit = CQLineEdit()

        self.step2Dialog = QDialog()
        self.step2Dialog.setLayout(self._buildStep2())
        self.step2Dialog.setWindowTitle('Operatör ve Proses giriniz...')
        # self.step1Dialog.setWindowFlag(Qt.FramelessWindowHint)
        # self.step1Dialog.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.step2Dialog.setWindowOpacity(0.9)
        self.step2Dialog.resize(600, 380)
        self.step2Dialog.exec()
        centerWidget(self.step2Dialog)

    #endregion




    # region STEP 1

    def _buildStep1(self):

        boxRoot = QVBoxLayout()

        self.txtWorkOrderNumber = CQLineEdit()
        self.txtWorkOrderNumber.setFont(fontSize20)
        self.txtWorkOrderNumber.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.txtWorkOrderNumber.setPlaceholderText('Ör: 19-123')
        self.txtWorkOrderNumber.clicked.connect(self.focusedLE)
        boxRoot.addWidget(self.txtWorkOrderNumber)

        gridNumpad = self._buildNumPad()

        btnHyphen = QPushButton('-')
        btnHyphen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnHyphen.setFont(fontSize20)
        btnHyphen.clicked.connect(self.btnClick_btnNumi)
        gridNumpad.addWidget(btnHyphen, 0, 3, 1, 1)

        btnDel = QPushButton('SİL')
        btnDel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnDel.setFont(fontSize20)
        btnDel.clicked.connect(self.btnClick_btnDel)
        gridNumpad.addWidget(btnDel, 1, 3, 2, 1)

        btnReject = QPushButton('KAPAT')
        btnReject.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnReject.setFont(fontSize20)
        btnReject.clicked.connect(lambda: self.btnClick_btnReject(self.step1Dialog))
        gridNumpad.addWidget(btnReject, 3, 0)

        btnNum0 = QPushButton('0')
        btnNum0.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnNum0.setFont(fontSize20)
        btnNum0.clicked.connect(self.btnClick_btnNumi)
        gridNumpad.addWidget(btnNum0, 3, 1)

        btnNextStep2 = QPushButton('DEVAM')
        btnNextStep2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnNextStep2.setFont(fontSize20)
        btnNextStep2.clicked.connect(self.btnClick_btnNextStep2)
        gridNumpad.addWidget(btnNextStep2, 3, 2, 1, 2)

        boxRoot.addLayout(gridNumpad)
        return boxRoot

    # endregion


    #region STEP 2

    def _buildStep2(self):

        gridNumpad = self._buildNumPad()
        gridInput = QGridLayout()
        boxRoot = QVBoxLayout()

        txtOperatorCode = CQLineEdit()
        txtOperatorCode.setObjectName('txtOperatorCode')
        txtOperatorCode.setFont(fontSize20)
        txtOperatorCode.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        txtOperatorCode.setPlaceholderText('Ör: 1686')
        txtOperatorCode.clicked.connect(self.focusedLE)
        gridInput.addWidget(txtOperatorCode, 0, 0, 1, 2)


        txtProcessCode = CQLineEdit()
        txtProcessCode.setObjectName('txtProcessCode')
        txtProcessCode.setFont(fontSize20)
        txtProcessCode.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        txtProcessCode.setPlaceholderText('Ör: 1001')
        txtProcessCode.clicked.connect(self.focusedLE)
        gridInput.addWidget(txtProcessCode, 0, 3, 1, 2)

        btnHyphen = QPushButton('-')
        btnHyphen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnHyphen.setFont(fontSize20)
        btnHyphen.clicked.connect(self.btnClick_btnNumi)
        gridNumpad.addWidget(btnHyphen, 0, 3, 1, 1)

        btnDel = QPushButton('SİL')
        btnDel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnDel.setFont(fontSize20)
        btnDel.clicked.connect(self.btnClick_btnDel)
        gridNumpad.addWidget(btnDel, 1, 3, 2, 1)

        btnReject = QPushButton('KAPAT')
        btnReject.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnReject.setFont(fontSize20)
        btnReject.clicked.connect(lambda: self.btnClick_btnReject(self.step2Dialog))
        gridNumpad.addWidget(btnReject, 3, 0)

        btnNum0 = QPushButton('0')
        btnNum0.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnNum0.setFont(fontSize20)
        btnNum0.clicked.connect(self.btnClick_btnNumi)
        gridNumpad.addWidget(btnNum0, 3, 1)

        btnAddOperator = QPushButton('EKLE')
        btnAddOperator.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnAddOperator.setFont(fontSize20)
        btnAddOperator.clicked.connect(lambda: self.btnClick_btnAddOperator(txtOperatorCode.text(), txtProcessCode.text()))
        gridNumpad.addWidget(btnAddOperator, 3, 2, 1, 2)

        boxRoot.addLayout(gridInput)
        boxRoot.addLayout(gridNumpad)

        return boxRoot

    #endregion



    #region UTILS

    def _buildNumPad(self):
        txtNum = 1
        gridNumpad = QGridLayout()

        for i in range(3):
            for j in range(3):
                btnNumi = QPushButton()
                btnNumi.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                btnNumi.setText(str(txtNum))
                btnNumi.clicked.connect(self.btnClick_btnNumi)
                btnNumi.setFont(fontSize20)
                txtNum = txtNum + 1
                gridNumpad.addWidget(btnNumi, i, j)
        return gridNumpad

    #endregion

    #region EVENTS

    def btnClick_btnNextStep2(self):
        self.btnClick_btnReject(self.step1Dialog)
        self._showDialogStep2()

    def btnClick_btnClose(self):
        self.close()

    def btnClick_btnReject(self, dialog):
        dialog.reject()

    def btnClick_btnNumi(self):
        btn = self.sender()
        self.focusedCQLineEdit.setText(self.focusedCQLineEdit.text() + btn.text())

    def btnClick_btnDel(self):
        self.focusedCQLineEdit.setText(self.focusedCQLineEdit.text()[:-1])

    def btnClick_btnAddOperator(self, valOperatorCode, valProcessCode):
        print('Operatör: ', str(valOperatorCode), ' - Proses: ', str(valProcessCode))
        self.btnClick_btnReject(self.step2Dialog)
        self._showDialogStep2()

    def focusedLE(self):
        print(self.sender())
        self.focusedCQLineEdit = self.sender()

    #endregion

def main():
    app = QApplication(sys.argv)
    production = Production()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



