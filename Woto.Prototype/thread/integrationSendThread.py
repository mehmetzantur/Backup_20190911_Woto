# -*- coding: utf-8 -*-
import os, sys, inspect, ctypes
from collections import deque

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from PyQt5.QtCore import QThread, pyqtSignal
from controller.pulseController import PulseController
from controller.integrationController import IntegrationController


class IntegrationSendThread(QThread):

    sendSignal = pyqtSignal(int)
    pulseController = PulseController()


    def __init__(self):
        super(IntegrationSendThread, self).__init__()
        # self.print_val = 0
        self.setTerminationEnabled(True)
        self.stopFlag = False
        self.isReady = True

    def stop(self):
        self.stopFlag = True

    def __del__(self):
        self.quit()
        self.wait()
    

    def run(self):
        print('tId: ' + str(self.currentThreadId()) + 'Integration Sending started...')

        while 1:
            if self.stopFlag == False:
                if self.isReady == True:
                    self.sendSignal.emit(1)
                    # IntegrationController().sendWaitingPulse()
                    self.isReady = IntegrationController().sendWaitingItems()
                    self.sleep(5)
                else:
                    print('SERVISE GONDERIM HAZIR DEGIL !')
            else:
                break

        print('tId: ' + str(self.currentThreadId()) + 'Integration Sending stopped... ')

