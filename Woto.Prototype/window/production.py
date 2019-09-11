# -*- coding: utf-8 -*-
import os, sys, inspect

from controller.integrationController import IntegrationController

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from collections import deque
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from thread.pulseReadThread import PulseReadThread
from thread.pulseWriteThread import PulseWriteThread
from thread.pulseSendThread import PulseSendThread
from thread.integrationSendThread import IntegrationSendThread



#region MODELS
from model.job import Job
from model.workerProcess import WorkerProcess
from model.viewModel.vmOperatorProcess import vmOperatorProcess
from model.pulse import Pulse
#endregion

#region CONTROLLERS
from controller.utilController import UtilController as util, Constant as const, WButton, WLed, WFooter, WHeader
from controller.workerController import WorkerController

#endregion


heightContent = 50




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

    startStopStatus = False
    pulseQueue = deque()
    thVal = 0

    def pulseRead(self):
        if self.thVal == 0:
            self.btnClick_btnStartStop()
            # self.PulseSendThread.start()
            self.IntegrationSendThread.start()
        self.pulseQueue.append(Pulse(None, self.jobId, util().getNow(), util().getUIID()))
        self.thVal = self.thVal + 1
        self.valCounter.setText(str(self.thVal) + ' / 0')


    def _buildUI(self, Window):

        self.PulseReadThread = PulseReadThread()
        self.PulseReadThread.pulseSignal.connect(self.pulseRead)
        self.PulseReadThread.start()

        # self.PulseWriteThread = PulseWriteThread(id(self.pulseQueue))
        # self.PulseWriteThread.start()

        self.IntegrationSendThread = IntegrationSendThread()


        self.focusedCQLineEdit = CQLineEdit()

        # region VARIABLES
        self.operatorProcessList = []
        self.operatorList = []
        self.lastOperatorCount = 0
        # endregion

        self.setLayout(self._buildMain())
        # self.show()
        self.showFullScreen()

        self._showDialogStep1()


    def _buildMain(self):

        self.setStyleSheet("background-color: " + const.color_smoothgray)

        boxRoot = QVBoxLayout()
        boxRoot.setContentsMargins(0, 0, 0, 0)
        boxRoot.setSpacing(0)

        widgetHeader = QWidget()
        widgetHeader.setFixedHeight(const.widgetHeaderHeight)
        widgetHeader.setStyleSheet("background-color: " + const.color_wgrBlue_hex)

        boxHeader = WHeader('ÜRETİM İZLEME', const.region)


        widgetHeader.setLayout(boxHeader)

        boxRoot.addWidget(widgetHeader)

        #region HEADER

        self.widgetStatusHeader = QWidget()
        self.widgetStatusHeader.setStyleSheet("color: white; background-color: " + const.color_darkgray_hex)
        self.widgetStatusHeader.setFixedHeight(const.widgetHeaderHeight)

        boxStatusHeader = QHBoxLayout()

        self.valJobOrderNumber = QLabel('EMİR BEKLENİYOR...')
        self.valJobOrderNumber.setContentsMargins(5, 0, 0, 0)
        self.valJobOrderNumber.setAlignment(Qt.AlignLeft)
        self.valJobOrderNumber.setFont(const.font_fontSize20)
        boxStatusHeader.addWidget(self.valJobOrderNumber)

        self.valCounter = QLabel('0 / 0')
        self.valCounter.setAlignment(Qt.AlignVCenter)
        self.valCounter.setAlignment(Qt.AlignHCenter)
        self.valCounter.setFont(const.font_fontSize20)
        self.valCounter.setText(str(self.thVal) + ' / 0')
        boxStatusHeader.addWidget(self.valCounter)

        self.valStatus = QLabel('ÇALIŞMIYOR')
        self.valStatus.setContentsMargins(0, 0, 5, 0)
        self.valStatus.setAlignment(Qt.AlignRight)
        self.valStatus.setFont(const.font_fontSize20)
        boxStatusHeader.addWidget(self.valStatus)

        # lineH = QFrame()
        # lineH.setFrameShape(QFrame.HLine)
        # lineH.setFrameShadow(QFrame.Sunken)
        # boxStatusHeader.addWidget(lineH)

        boxStatusHeader.setAlignment(Qt.AlignTop)

        self.widgetStatusHeader.setLayout(boxStatusHeader)

        boxRoot.addWidget(self.widgetStatusHeader)

        #endregion

        #region CONTENT

        gridContent = QGridLayout()

        self.tableWorker = QTableWidget()
        self.tableWorker.setStyleSheet('background-color: white;')
        self.tableWorker.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWorker.setCornerButtonEnabled(True)
        self.tableWorker.setSortingEnabled(True)

        gridContent.addWidget(self.tableWorker, 1, 0, 1, 3)

        boxRoot.addLayout(gridContent)

        #endregion

        #region FOOTER

        gridFooter = QGridLayout()
        gridFooter.setAlignment(Qt.AlignBottom)

        lineB = QFrame()
        lineB.setFrameShape(QFrame.HLine)
        lineB.setFrameShadow(QFrame.Sunken)
        gridFooter.addWidget(lineB, 0, 0, 1, 3)

        btnClose = WButton('KAPAT')
        btnClose.clicked.connect(self.btnClick_btnClose)
        btnClose.setFixedHeight(70)
        gridFooter.addWidget(btnClose, 1, 0)

        self.btnStartStop = WButton('BAŞLA')
        self.btnStartStop.setDisabled(True)
        self.btnStartStop.clicked.connect(self.btnClick_btnStartStop)
        self.btnStartStop.setFixedHeight(70)
        gridFooter.addWidget(self.btnStartStop, 1, 1)

        self.btnCounterReset = WButton('SIFIRLA')
        self.btnCounterReset.clicked.connect(self.btnClick_btnCounterReset)
        self.btnCounterReset.setFixedHeight(70)
        gridFooter.addWidget(self.btnCounterReset, 2, 1)

        gridAddDeleteOperator = QGridLayout()

        self.btnAddOperator = WButton('(+) OPT/PRS')
        self.btnAddOperator.setDisabled(True)
        self.btnAddOperator.clicked.connect(self._showDialogStep2)
        self.btnAddOperator.setFixedHeight(70)
        gridAddDeleteOperator.addWidget(self.btnAddOperator, 0, 0)

        self.btnDeleteOperator = WButton('(-) OPT/PRS')
        self.btnDeleteOperator.setDisabled(True)
        self.btnDeleteOperator.clicked.connect(self.deleteOperatorProcess)
        self.btnDeleteOperator.setFixedHeight(70)
        gridAddDeleteOperator.addWidget(self.btnDeleteOperator, 0, 1)

        gridFooter.addLayout(gridAddDeleteOperator, 1, 2)

        btnStance = WButton('DURUŞ')
        # btnStance.clicked.connect(self.btnClick_btnClose)
        btnStance.setFixedHeight(70)
        gridFooter.addWidget(btnStance, 2, 2)

        boxRoot.addLayout(gridFooter)

        widgetFooter = QWidget()
        widgetFooter.setFixedHeight(30)
        widgetFooter.setStyleSheet("background-color: " + const.color_wgrBlue_hex)

        boxFooter = WFooter()

        widgetFooter.setLayout(boxFooter)

        boxRoot.addWidget(widgetFooter)

        #endregion

        return boxRoot




    #region STEP DIALOGS

    def _showDialogStep1(self):



        self.step1Dialog = QDialog()
        self.step1Dialog.setStyleSheet("QDialog { border:4px solid " + const.color_wgrBlue_hex + "  background-color: " + const.color_smoothgray + "}")
        self.step1Dialog.setLayout(self._buildStep1())
        self.step1Dialog.setWindowTitle('Emir No giriniz...')
        self.step1Dialog.setWindowFlag(Qt.FramelessWindowHint)
        self.step1Dialog.setWindowFlag(Qt.WindowCloseButtonHint, False)

        self.step1Dialog.resize(600, 400)
        self.step1Dialog.exec()
        # self.step1Dialog.showFullScreen()

        centerWidget(self.step1Dialog)
        self.step1Dialog.setContentsMargins(0, 0, 0, 0)



    def _showDialogStep2(self):



        self.step2Dialog = QDialog()
        self.step2Dialog.setStyleSheet("QDialog { border:4px solid " + const.color_wgrBlue_hex + "  background-color: " + const.color_smoothgray + "}")
        self.step2Dialog.setLayout(self._buildStep2())
        self.step2Dialog.setWindowTitle('Operatör ve Proses giriniz...')
        self.step2Dialog.setWindowFlag(Qt.FramelessWindowHint)
        self.step2Dialog.setWindowFlag(Qt.WindowCloseButtonHint, False)

        self.step2Dialog.resize(600, 400)
        self.step2Dialog.exec()
        # self.step2Dialog.showFullScreen()

        centerWidget(self.step2Dialog)
        self.step1Dialog.setContentsMargins(0, 0, 0, 0)

    #endregion





    # region STEP 1

    def _buildStep1(self):

        boxRoot = QVBoxLayout()
        boxRoot.setContentsMargins(0, 0, 0, 0)

        widgetHeader = QWidget()
        widgetHeader.setFixedHeight(50)
        widgetHeader.setStyleSheet("background-color: " + const.color_wgrBlue_hex)


        boxHeader = QHBoxLayout()

        labelTitle = QLabel('EMİR GİRİNİZ...')
        labelTitle.setFont(const.font_fontSize15)
        labelTitle.setStyleSheet("color: white;")
        labelTitle.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        boxHeader.addWidget(labelTitle)

        widgetHeader.setLayout(boxHeader)

        boxRoot.addWidget(widgetHeader)

        gridInput = QGridLayout()
        gridInput.setContentsMargins(5, 5, 5, 5)

        txtJobOrderNumber = CQLineEdit()
        txtJobOrderNumber.setContentsMargins(5, 5, 5, 0)
        txtJobOrderNumber.setStyleSheet("border-radius: 3px; background-color:white;")
        txtJobOrderNumber.setFont(const.font_fontSize20)
        txtJobOrderNumber.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        txtJobOrderNumber.setPlaceholderText('Ör: 19-123')
        txtJobOrderNumber.clicked.connect(lambda: self.focusedLE(txtJobOrderNumber))
        gridInput.addWidget(txtJobOrderNumber, 0, 0)
        boxRoot.addLayout(gridInput)
        self.focusedLE(txtJobOrderNumber)

        gridNumpad = self._buildNumPad()
        gridNumpad.setContentsMargins(5, 5, 5, 5)

        btnHyphen = WButton('-')
        btnHyphen.clicked.connect(self.btnClick_btnNumi)
        gridNumpad.addWidget(btnHyphen, 0, 3, 1, 1)

        btnDel = WButton('SİL')
        btnDel.clicked.connect(self.btnClick_btnDel)
        gridNumpad.addWidget(btnDel, 1, 3, 2, 1)

        btnReject = WButton('KAPAT')
        btnReject.clicked.connect(lambda: self.btnClick_btnReject(self.step1Dialog))
        gridNumpad.addWidget(btnReject, 3, 0)

        btnNum0 = WButton('0')
        btnNum0.clicked.connect(self.btnClick_btnNumi)
        gridNumpad.addWidget(btnNum0, 3, 1)

        btnNextStep2 = WButton('DEVAM')
        btnNextStep2.clicked.connect(lambda: self.btnClick_btnNextStep2(txtJobOrderNumber.text()))
        gridNumpad.addWidget(btnNextStep2, 3, 2, 1, 2)

        boxRoot.addLayout(gridNumpad)
        return boxRoot

    # endregion


    #region STEP 2

    def _buildStep2(self):

        gridNumpad = self._buildNumPad()
        gridNumpad.setContentsMargins(5, 5, 5, 5)
        gridInput = QGridLayout()
        gridInput.setContentsMargins(5, 0, 5, 0)
        boxRoot = QVBoxLayout()
        boxRoot.setContentsMargins(0, 0, 0, 0)


        widgetHeader = QWidget()
        widgetHeader.setFixedHeight(50)
        widgetHeader.setStyleSheet("background-color: " + const.color_wgrBlue_hex)

        boxHeader = QHBoxLayout()

        labelTitle = QLabel('SİCİL ve PROSES GİRİNİZ...')
        labelTitle.setFont(const.font_fontSize15)
        labelTitle.setStyleSheet("color: white;")
        labelTitle.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        boxHeader.addWidget(labelTitle)

        widgetHeader.setLayout(boxHeader)

        boxRoot.addWidget(widgetHeader)

        self.txtOperatorCode = CQLineEdit()
        self.count_txtOperatorCode = 0
        self.txtOperatorCode.setObjectName('txtOperatorCode')
        self.txtOperatorCode.setContentsMargins(5, 5, 5, 0)
        self.txtOperatorCode.setStyleSheet("border-radius: 3px; background-color:white;")
        self.txtOperatorCode.setFont(const.font_fontSize20)
        self.txtOperatorCode.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.txtOperatorCode.setPlaceholderText('Ör: 1686')
        self.txtOperatorCode.clicked.connect(lambda: self.focusedLE(self.txtOperatorCode))
        self.txtOperatorCode.textChanged.connect(self.txtChanged_txtOperatorCode)
        gridInput.addWidget(self.txtOperatorCode, 0, 0, 1, 2)
        self.focusedLE(self.txtOperatorCode)


        self.txtProcessCode = CQLineEdit()
        self.txtProcessCode.setObjectName('txtProcessCode')
        self.txtProcessCode.setContentsMargins(5, 5, 5, 0)
        self.txtProcessCode.setStyleSheet("border-radius: 3px; background-color:white;")
        self.txtProcessCode.setFont(const.font_fontSize20)
        self.txtProcessCode.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.txtProcessCode.setPlaceholderText('Ör: 1001')
        self.txtProcessCode.clicked.connect(lambda: self.focusedLE(self.txtProcessCode))
        self.txtProcessCode.textChanged.connect(self.txtChanged_txtProcessCode)
        gridInput.addWidget(self.txtProcessCode, 0, 3, 1, 2)

        btnHyphen = WButton('-')
        btnHyphen.setDisabled(True)
        btnHyphen.clicked.connect(self.btnClick_btnNumi)
        gridNumpad.addWidget(btnHyphen, 0, 3, 1, 1)

        btnDel = WButton('SİL')
        btnDel.clicked.connect(self.btnClick_btnDel)
        gridNumpad.addWidget(btnDel, 1, 3, 2, 1)

        btnReject = WButton('KAPAT')
        btnReject.clicked.connect(self.btnClick_btnSubmitOperators)
        gridNumpad.addWidget(btnReject, 3, 0)

        btnNum0 = WButton('0')
        btnNum0.clicked.connect(self.btnClick_btnNumi)
        gridNumpad.addWidget(btnNum0, 3, 1)

        btnAddOperator = WButton('EKLE')
        btnAddOperator.clicked.connect(lambda: self.btnClick_btnAddOperator(self.txtOperatorCode.text(), self.txtProcessCode.text()))
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
                btnNumi = WButton(str(txtNum))
                btnNumi.clicked.connect(self.btnClick_btnNumi)
                txtNum = txtNum + 1
                gridNumpad.addWidget(btnNumi, i, j)
        return gridNumpad

    #endregion

    #region EVENTS

    def deleteOperatorProcess(self):



        rowtext = []
        indexes = self.tableWorker.selectionModel().selectedRows()
        for index in sorted(indexes):
            row = index.row()

            for column in range(self.tableWorker.columnCount()):
                rowtext.append(self.tableWorker.item(row, column).text())
            # print('secilen satir: ' + str(rowtext))

        if len(rowtext) > 0:

            # print('--------------------deleteOperatorProcess baslangici--------------------')

            # print('son durum operatorProcessList: ' + str(len(self.operatorProcessList)))

            for item in self.operatorProcessList:
                if item.operatorCode == rowtext[2] and item.processCode == rowtext[3]:
                    self.operatorProcessList.remove(item)
                    # print('silinen: ' + item.operatorCode + ' , ' + item.processCode)

            # print('güncel operatorProcessList: ' + str(len(self.operatorProcessList)))

            operatorTempList = []
            for item in self.operatorProcessList:
                if item.operatorCode not in operatorTempList:
                    operatorTempList.append(item.operatorCode)

            # print('operatorList: ' + str(self.operatorList))
            # print('aktarildi, operatorTempList: ' + str(operatorTempList))

            # print(str(self.operatorList) + ' == ' + str(operatorTempList))



            if operatorTempList.count(rowtext[2]) == 0:
                self.operatorList.remove(rowtext[2])
                # print('operatorList icindeki operator silindi')
                #operatorTempList = self.operatorList
                #print('operatorTempList içindeki operatör kodu silindi')
                self.lastOperatorCount = self.lastOperatorCount - 1

            # print('güncel operatorList: ' + str(len(self.operatorList)))
            # print('güncel operatorProcessList: ' + str(len(self.operatorProcessList)))

            selectedRow = self.tableWorker.currentRow()
            self.tableWorker.removeRow(selectedRow)

            self.btnClick_btnSubmitOperators()

            # print('--------------------deleteOperatorProcess bitisi--------------------')

    def btnClick_btnNextStep2(self, jobOrderNumber):
        if jobOrderNumber.strip() != "":
            self.btnStartStop.setEnabled(True)
            self.btnAddOperator.setEnabled(True)
            self.btnDeleteOperator.setEnabled(True)
            self.valJobOrderNumber.setText(jobOrderNumber)
            self.btnClick_btnReject(self.step1Dialog)
            self.step1Dialog.close()
            self._showDialogStep2()

    def btnClick_btnClose(self):
        self.operatorProcessList = []
        self.operatorList = []
        self.lastOperatorCount = 0
        self.tableWorker.clear()
        # print(str(len(self.operatorProcessList)))
        # print(str(len(self.operatorList)))
        self.PulseWriteThread.stop()
        self.PulseWriteThread.stop()
        self.PulseSendThread.stop()
        self.close()

    def btnClick_btnReject(self, dialog):
        dialog.close()

    def btnClick_btnNumi(self):
        btn = self.sender()
        self.focusedCQLineEdit.setText(self.focusedCQLineEdit.text() + btn.text())

    def btnClick_btnDel(self):
        self.focusedCQLineEdit.setText(self.focusedCQLineEdit.text()[:-1])
        
    def btnClick_btnStartStop(self):
        if self.startStopStatus == True:
            self.btnStartStop.setText('BAŞLAT')
            self.valStatus.setText('ÇALIŞMIYOR')
            self.widgetStatusHeader.setStyleSheet("color: white; background-color: " + const.color_darkgray_hex)
            self.startStopStatus = False
        else:
            self.btnStartStop.setText('DURDUR')
            self.valStatus.setText('ÇALIŞIYOR')
            self.widgetStatusHeader.setStyleSheet("color: white; background-color: " + const.color_success_hex)
            self.startStopStatus = True

    def btnClick_btnCounterReset(self):
        self.thVal = 0
        self.valCounter.setText('0 / 0')

    def btnClick_btnAddOperator(self, operatorCode, processCode):
        if len(operatorCode) == 4 and len(processCode) == 4:
            objOperatorProcess = vmOperatorProcess(operatorCode, processCode)
            self.operatorProcessList.append(objOperatorProcess)
            if operatorCode not in self.operatorList:
                self.operatorList.append(operatorCode)

            self.btnClick_btnReject(self.step2Dialog)
            self._showDialogStep2()

    def btnClick_btnSubmitOperators(self):

        # print('-----submit----')
        # print(str(len(self.operatorProcessList)))
        # print(str(len(self.operatorList)))
        # print(str(self.lastOperatorCount))

        if len(self.operatorProcessList) != self.lastOperatorCount:
            if len(self.operatorList) > 0:

                # for item in self.operatorProcessList:
                    # print(item.operatorCode + ' - ' + item.processCode)

                self.jobId = WorkerController().createWorker(self.valJobOrderNumber.text(), self.operatorList, self.operatorProcessList)

                self.lastOperatorCount = len(self.operatorProcessList)

                self.tableWorker.clear()
                self.tableWorker.setRowCount(0)
                self.tableWorker.setColumnCount(5)

                for row_number, row_data in enumerate(WorkerController().getWorkersForJobOrderNumber(self.jobId)):
                    self.tableWorker.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWorker.setItem(row_number, column_number, QTableWidgetItem(str(data)))

                self.tableWorker.setHorizontalHeaderItem(0, QTableWidgetItem('WP Id'))
                self.tableWorker.setHorizontalHeaderItem(1, QTableWidgetItem('Job Id'))
                self.tableWorker.setHorizontalHeaderItem(2, QTableWidgetItem('OperatorId'))
                self.tableWorker.setHorizontalHeaderItem(3, QTableWidgetItem('ProcessId'))
                self.tableWorker.setHorizontalHeaderItem(4, QTableWidgetItem('CreatedId'))

            else:
                self.tableWorker.clear()
                self.tableWorker.setRowCount(0)
                self.tableWorker.setColumnCount(5)

                self.tableWorker.setHorizontalHeaderItem(0, QTableWidgetItem('WP Id'))
                self.tableWorker.setHorizontalHeaderItem(1, QTableWidgetItem('Job Id'))
                self.tableWorker.setHorizontalHeaderItem(2, QTableWidgetItem('OperatorId'))
                self.tableWorker.setHorizontalHeaderItem(3, QTableWidgetItem('ProcessId'))
                self.tableWorker.setHorizontalHeaderItem(4, QTableWidgetItem('CreatedId'))

        self.btnClick_btnReject(self.step2Dialog)

    def focusedLE(self, txtObject):
        # print(txtObject)
        self.focusedCQLineEdit = txtObject

    #endregion


    def txtChanged_txtOperatorCode(self):
        if len(self.txtOperatorCode.text()) == 4:
            self.txtProcessCode.setFocus()
            self.focusedLE(self.txtProcessCode)



    def txtChanged_txtProcessCode(self):
        if len(self.txtProcessCode.text()) == 4:
            self.btnClick_btnAddOperator(self.txtOperatorCode.text(), self.txtProcessCode.text())



def main():
    app = QApplication(sys.argv)
    production = Production()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



