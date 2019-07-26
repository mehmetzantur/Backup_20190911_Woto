import time
import RPi.GPIO as GPIO
from PyQt5.QtCore import QThread, pyqtSignal


class PulseThread(QThread):

    pulseSignal = pyqtSignal(int)



    def __init__(self):
        super(PulseThread, self).__init__()
        # self.print_val = 0
        self.setTerminationEnabled(True)




    def __del__(self):
        self.wait()

    def run(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.IN)
        print('started...')

        while 1:
            if GPIO.input(11) == True:
                self.pulseSignal.emit(1)
                while 1:
                    if GPIO.input(11) == True:
                        continue
                    else:
                        break



    def started(self):
        print('ThreadId: ' + str(self.currentThreadId()) + ' is started.')

    def stop(self):
        self.terminate()
        print('ThreadId: ' + str(self.currentThreadId()) + ' is terminated.')


    def finished(self):
        print('ThreadId: ' + str(self.currentThreadId()) + ' is finished.')


    def doProcess(self, val):
        print(str(val))
