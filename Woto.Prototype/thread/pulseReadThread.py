import time
import RPi.GPIO as GPIO
from PyQt5.QtCore import QThread, pyqtSignal


class PulseReadThread(QThread):

    pulseSignal = pyqtSignal(int)



    def __init__(self):
        super(PulseReadThread, self).__init__()
        # self.print_val = 0
        self.setTerminationEnabled(True)
        self.stopFlag = False

    def stop(self):
        self.stopFlag = True

    def __del__(self):
        self.quit()
        self.wait()

    def run(self):
        counter = 0
        counterx = 1
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

        print('Pulse listening is started...')

        while 1:
            if self.stopFlag == False:
                # if GPIO.input(11) == 1 and counterx == 1:
                if counterx == 1:
                    # self.pulseSignal.emit(1)
                    # counterx = 0
                    # counter = counter + 1
                    # print('pulse ' + str(counter))

                    # while 1:

                    #     if GPIO.input(11) == 1 and counterx == 1:
                    #         counterx = 0
                    #         pass

                    #     if GPIO.input(11) == 0 and counterx == 0:
                    #         counterx = 1
                    #         time.sleep(0.1)
                    #         break
                    print('plssss')
            else:
                break

        print('Pulse listening is stopped...')

