# -*- coding: utf-8 -*-
import os, sys, inspect, requests, json
from time import sleep

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from controller.dbController import DbController
from controller.utilController import UtilController as util, Constant as const

from model.pulse import Pulse

class IntegrationController:
    serviceUrl = "http://websrv:85/Woto.WebService/api/integration/"
    serviceUrlLocal = "http://localhost:5588/api/integration/"

    headers = {'Content-type': 'application/json'}



    def sendWaitingPulse(self):

        pulseList = self.getWaitingToSendPulseList()
        if len(pulseList) > 0:
            jsonPulseList = util().serializeListToJson(pulseList)
            result = requests.post(self.serviceUrl + "AddPulse", data=jsonPulseList, headers=self.headers)
            if result.status_code == 200:
                print('Sending to service is successful.')

                updateStatus = []
                for item in result.json():
                    itemPulse = Pulse(**item)
                    updateStatus.append(self.updateSendedPulse(itemPulse.id))

                if False in updateStatus:
                    print('Update yaparken hata oluştu!')
                    return False

                print('Güncelleme başarılı.')
                return True

    def updateSendedPulse(self, id):

        try:
            conn = DbController().getConnection()
            cmd = conn.cursor()
            cmd.execute("UPDATE Pulse SET IsSended = 1 WHERE Id = ?", (id,))
            conn.commit()
        except:
            return False
        finally:
            conn.close()

        return True

    def getWaitingToSendPulseList(self):
        conn = DbController().getConnection()
        cmd = conn.cursor()
        query_getWaitingToSendPulseList = "SELECT * FROM Pulse WHERE IsSended = 0"
        cmd.execute(query_getWaitingToSendPulseList)
        pulseList = []
        for item in cmd.fetchall():
            pulseItem = Pulse(item[0], item[1], item[2], item[3], item[4])
            pulseList.append(pulseItem)

        return pulseList
