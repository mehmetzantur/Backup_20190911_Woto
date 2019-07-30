# -*- coding: utf-8 -*-
import os, sys, inspect, ctypes
from collections import deque

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from PyQt5.QtCore import QThread, pyqtSignal
from controller.pulseController import PulseController


class PulseTickThread(QThread):

    pulseSignal = pyqtSignal(int)



    def __init__(self, valAddress):
        super(PulseTickThread, self).__init__()
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
        que = ctypes.cast(self.valAddress, ctypes.py_object).value
        while 1:
            if self.stopFlag == False:
                if que.count > 0:
                    self.pulseSignal.emit(1)
                    print(que.popleft())
                    que = list(ctypes.cast(self.valAddress, ctypes.py_object).value)
                    print(que)
                self.sleep(3)
            else:
                break

        # pulseController = PulseController()
        # rowid = pulseController.createPulse(self.jobId)

        print('tId: ' + str(self.currentThreadId()) + 'Writing stopped... ')

