from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from productionWindow import ProductionWindow

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

class MenuWindow(QWidget):


    def __init__(self):
        super(MenuWindow, self).__init__()

        self.showDialogForWorkOrderNumberHasLayout = False

        self.txtWorkOrderNumber = QLineEdit()
        self.txtWorkOrderNumber.setFont(fontSize20)
        self.txtWorkOrderNumber.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.txtWorkOrderNumber.setPlaceholderText('19-123')

        self.numpadGrid = QGridLayout()
        self.myDialogVBox = QVBoxLayout()
        self.myDialogVBox.addWidget(self.txtWorkOrderNumber)

        self.setFixedSize(piResolutionWidth, piResolutionHeight)
        self.setWindowTitle('Woto MENÜ')
        centerWidget(self)
        self.setLayout(self.buildMenu())

        self.myDialog = QDialog()

        self.myDialog.setWindowTitle('EMİR NO GİRİNİZ - ÜRETİM BAŞLAT')
        self.myDialog.setModal(True)
        self.myDialog.setFixedSize(400, piResolutionHeight)
        self.myDialog.setWindowFlag(Qt.WindowCloseButtonHint, False)
        centerWidget(self.myDialog)

        self.show()



    # MENÜ ızgarasını oluşturur.
    def buildMenu(self):

        btnStartProduction = QPushButton('ÜRETİM BAŞLAT')
        btnStartProduction.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnStartProduction.clicked.connect(self.showDialogForWorkOrderNumber)
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

        btnMenu9 = QPushButton('MENÜ9')
        btnMenu9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnMenu9.setFont(fontSize20)

        menuGrid = QGridLayout()
        menuGrid.addWidget(btnStartProduction, 0, 0)
        menuGrid.addWidget(btnMenu2, 0, 1)
        menuGrid.addWidget(btnMenu3, 0, 2)
        menuGrid.addWidget(btnMenu4, 1, 0)
        menuGrid.addWidget(btnMenu5, 1, 1)
        menuGrid.addWidget(btnMenu6, 1, 2)
        menuGrid.addWidget(btnMenu7, 2, 0)
        menuGrid.addWidget(btnMenu8, 2, 1)
        menuGrid.addWidget(btnMenu9, 2, 2)

        return menuGrid

    # Emir no girişi için Dialog penceresi açar.
    def showDialogForWorkOrderNumber(self):

        # GRID NumPad
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

        btnHyphen = QPushButton('-')
        btnHyphen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnHyphen.setFont(fontSize20)
        btnHyphen.clicked.connect(self.btnClick_btnNumi)
        self.numpadGrid.addWidget(btnHyphen, 0, 3, 1, 1)

        btnDel = QPushButton('SİL')
        btnDel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnDel.setFont(fontSize20)
        btnDel.clicked.connect(self.btnClick_btnDel)
        self.numpadGrid.addWidget(btnDel, 1, 3, 2, 1)

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

        # ---------------------------------------------------------------

        if self.showDialogForWorkOrderNumberHasLayout == False:
            self.myDialogVBox.addLayout(self.numpadGrid)
            self.myDialog.setLayout(self.myDialogVBox)
            self.showDialogForWorkOrderNumberHasLayout = True
        self.myDialog.exec()

    def btnClick_btnClose(self):
        self.txtWorkOrderNumber.setText('')
        self.myDialog.reject()

    def btnClick_btnNumi(self):
        btn = self.sender()
        self.txtWorkOrderNumber.setText(self.txtWorkOrderNumber.text() + btn.text())

    def btnClick_btnDel(self):
        self.txtWorkOrderNumber.setText(self.txtWorkOrderNumber.text()[:-1])

    def btnClick_btnNext(self):
        self.btnClick_btnClose()
        self.productionWindow = QDialog()
        self.ui = ProductionWindow()
        self.ui.setupUi(self.productionWindow)
        self.productionWindow.show()


def main():
    app = QApplication(sys.argv)
    mainWindow = MenuWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()




