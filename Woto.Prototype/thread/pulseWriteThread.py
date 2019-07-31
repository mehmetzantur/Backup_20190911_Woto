# -*- coding: utf-8 -*-
import os, sys, inspect, ctypes
from collections import deque

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from PyQt5.QtCore import QThread, pyqtSignal
from controller.pulseController import PulseController
from controller.utilController import UtilController


class PulseWriteThread(QThread):

    pulseSignal = pyqtSignal(int)
    pulseController = PulseController()


    def __init__(self, valAddress):
        super(PulseWriteThread, self).__init__()
        # self.print_val = 0
        self.setTerminationEnabled(True)
        self.stopFlag = False
        self.valAddress = valAddress

    def stop(self):
        self.stopFlag = True

    def __del__(self):
        self.quit()
        self.wait()

    def run(self):
        print('tId: ' + str(self.currentThreadId()) + 'Writing started...')
        print('address: ' + str(self.valAddress))
        que = UtilController().getObjectFromMemory(self.valAddress)
        while 1:
            if self.stopFlag == False:
                if len(que) > 0:
                    self.pulseSignal.emit(1)
                    pulseObj = que.popleft()
                    lastrowid = self.pulseController.createPulse(pulseObj.jobId)
                    print(lastrowid)
                    queList = list(UtilController().getObjectFromMemory(self.valAddress))
                    print(queList)
                self.sleep(.5)
            else:
                break

        # pulseController = PulseController()
        # rowid = pulseController.createPulse(self.jobId)

        print('tId: ' + str(self.currentThreadId()) + 'Writing stopped... ')

