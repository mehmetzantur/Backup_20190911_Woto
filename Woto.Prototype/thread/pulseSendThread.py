# -*- coding: utf-8 -*-
import os, sys, inspect, ctypes
from collections import deque

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from PyQt5.QtCore import QThread, pyqtSignal
from controller.pulseController import PulseController
from controller.integrationController import IntegrationController


class PulseSendThread(QThread):

    sendSignal = pyqtSignal(int)
    pulseController = PulseController()


    def __init__(self):
        super(PulseSendThread, self).__init__()
        # self.print_val = 0
        self.setTerminationEnabled(True)
        self.stopFlag = False

    def stop(self):
        self.stopFlag = True

    def __del__(self):
        self.quit()
        self.wait()

    def run(self):
        print('tId: ' + str(self.currentThreadId()) + 'Sending started...')

        while 1:
            if self.stopFlag == False:
                self.sendSignal.emit(1)
                IntegrationController().sendWaitingPulse()
                self.sleep(.5)
            else:
                break

        # pulseController = PulseController()
        # rowid = pulseController.createPulse(self.jobId)

        print('tId: ' + str(self.currentThreadId()) + 'Sending stopped... ')

