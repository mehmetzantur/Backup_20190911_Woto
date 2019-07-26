import time

from PyQt5.QtCore import QThread, pyqtSignal


class DenemeThread(QThread):

    mySinyal = pyqtSignal(int)

    myTerminatedSinyal = pyqtSignal(bool)

    def __init__(self):
        super(DenemeThread, self).__init__()
        # self.print_val = 0




    def __del__(self):
        self.wait()

    def run(self):
        for i in range(30):
            # self.doProcess(i)
            self.mySinyal.emit(i)
            time.sleep(1)


    def started(self):
        print('ThreadId: ' + str(self.currentThreadId()) + ' is started.')

    def terminate(self):
        super(DenemeThread, self).terminate()
        print('ThreadId: ' + str(self.currentThreadId()) + ' is terminated.')


    def finished(self):
        print('ThreadId: ' + str(self.currentThreadId()) + ' is finished.')


    def doProcess(self, val):
        print(str(val))
