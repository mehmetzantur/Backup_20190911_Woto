# -*- coding: utf-8 -*-
import os, sys, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from PyQt5.QtCore import QThread, pyqtSignal
from controller.pulseController import PulseController


class PulseWriteThread(QThread):

    #pulseSignal = pyqtSignal(int)



    def __init__(self, jobId):
        super(PulseWriteThread, self).__init__()
        # self.print_val = 0
        self.setTerminationEnabled(True)
        self.stopFlag = False
        self.jobId = jobId

    def stop(self):
        self.stopFlag = True

    def __del__(self):
        self.quit()
        self.wait()

    def run(self):
        print('tId: ' + str(self.currentThreadId()) + 'Writing started...')

        pulseController = PulseController()
        rowid = pulseController.createPulse(self.jobId)

        print('tId: ' + str(self.currentThreadId()) + 'Writing stopped... ' + rowid)

