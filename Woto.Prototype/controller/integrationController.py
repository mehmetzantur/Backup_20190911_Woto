# -*- coding: utf-8 -*-
import os, sys, inspect, requests, json
from time import sleep

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from controller.dbController import DbController
from controller.utilController import UtilController as util, Constant as const

from model.job import Job
from model.worker import Worker
from model.workerProcess import WorkerProcess
from model.pulse import Pulse

class IntegrationController:
    serviceUrl = "http://websrv:85/Woto.WebService/api/integration/"
    serviceUrlLocal = "http://localhost:5588/api/integration/"

    headers = {'Content-type': 'application/json'}

    def sendWaitingItems(self):
        isSendStatus = 0
        # isSendStatus += int(self.sendWaitingJob())
        # isSendStatus += int(self.sendWaitingWorker())
        # isSendStatus += int(self.sendWaitingWorkerProcess())
        # isSendStatus += int(self.sendWaitingPulse())

        self.sendWaitingJob()
        self.sendWaitingWorker()
        # self.sendWaitingWorkerProcess()
        # self.sendWaitingPulse()

        # if isSendStatus == 4:
        #     return True
        # else:
        #     return False

        return True

    #region JOB SEND OPERATIONS

    def sendWaitingJob(self):
        print('send waiting job started')
        jobList = self.getWaitingToSendJobList()
        if len(jobList) > 0:
            jsonJobList = util().serializeListToJson(jobList)
            result = requests.post(self.serviceUrl + "AddJob", data=jsonJobList, headers=self.headers)
            print('servis sonucu: ' + str(result.status_code))
            if result.status_code == 200:
                print('Job sending to service is successful.')

                updateStatus = []
                for item in result.json():
                    itemJob = Job(**item)
                    print('update id si: ' + str(itemJob.id))
                    updateStatus.append(self.updateSendedJob(itemJob.id))

                if False in updateStatus:
                    print('Job Update yaparken hata oluştu!')
                    return 0

                print('Job Update successful.')
                return 1

    def updateSendedJob(self, id):

        try:
            conn = DbController().getConnection()
            cmd = conn.cursor()
            cmd.execute("UPDATE Job SET IsSended = 1 WHERE Id = ?", (id,))
            conn.commit()
        except:
            return False
        finally:
            conn.close()

        return True

    def getWaitingToSendJobList(self):
        conn = DbController().getConnection()
        cmd = conn.cursor()
        query_getWaitingToSendJobList = "SELECT * FROM Job WHERE IsSended = 0"
        cmd.execute(query_getWaitingToSendJobList)
        jobList = []
        for item in cmd.fetchall():
            jobItem = Job(item[0], item[1], item[2], item[3], item[4], item[5])
            jobList.append(jobItem)

        # print(jobList[0].id)
        return jobList

    #endregion




    # region WORKER SEND OPERATIONS

    def sendWaitingWorker(self):

        workerList = self.getWaitingToSendWorkerList()
        if len(workerList) > 0:
            jsonWorkerList = util().serializeListToJson(workerList)
            result = requests.post(self.serviceUrl + "AddWorker", data = jsonWorkerList, headers = self.headers)
            if result.status_code == 200:
                print('Worker Sending to service is successful.')

                updateStatus = []
                for item in result.json():
                    itemWorker = Worker(**item)
                    updateStatus.append(self.updateSendedWorker(itemWorker.id))

                if False in updateStatus:
                    print('Worker Update yaparken hata oluştu!')
                    return 0

                print('Worker Update successful.')
                return 1

    def updateSendedWorker(self, id):

        try:
            conn = DbController().getConnection()
            cmd = conn.cursor()
            cmd.execute("UPDATE Worker SET IsSended = 1 WHERE Id = ?", (id,))
            conn.commit()
        except:
            return False
        finally:
            conn.close()

        return True

    def getWaitingToSendWorkerList(self):
        conn = DbController().getConnection()
        cmd = conn.cursor()
        query_getWaitingToSendWorkerList = "SELECT * FROM Worker WHERE IsSended = 0"
        cmd.execute(query_getWaitingToSendWorkerList)
        workerList = []
        for item in cmd.fetchall():
            workerItem = Worker(item[0], item[1], item[2], item[3], item[4], item[5])
            workerList.append(workerItem)

        return workerList

    # endregion




    # region WORKERProcess SEND OPERATIONS

    def sendWaitingWorkerProcess(self):

        workerProcessList = self.getWaitingToSendWorkerProcessList()
        if len(workerProcessList) > 0:
            jsonWorkerProcessList = util().serializeListToJson(workerProcessList)
            result = requests.post(self.serviceUrl + "AddWorkerProcess", data = jsonWorkerProcessList, headers = self.headers)
            if result.status_code == 200:
                print('WorkerProcess Sending to service is successful.')

                updateStatus = []
                for item in result.json():
                    itemWorkerProcess = WorkerProcess(**item)
                    updateStatus.append(self.updateSendedWorkerProcess(itemWorkerProcess.id))

                if False in updateStatus:
                    print('WorkerProcess Update yaparken hata oluştu!')
                    return 0

                print('WorkerProcess Update successful.')
                return 1

    def updateSendedWorkerProcess(self, id):

        try:
            conn = DbController().getConnection()
            cmd = conn.cursor()
            cmd.execute("UPDATE WorkerProcess SET IsSended = 1 WHERE Id = ?", (id,))
            conn.commit()
        except:
            return False
        finally:
            conn.close()

        return True

    def getWaitingToSendWorkerProcessList(self):
        conn = DbController().getConnection()
        cmd = conn.cursor()
        query_getWaitingToSendWorkerProcessList = "SELECT * FROM WorkerProcess WHERE IsSended = 0"
        cmd.execute(query_getWaitingToSendWorkerProcessList)
        workerProcessList = []
        for item in cmd.fetchall():
            workerProcessItem = WorkerProcess(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            workerProcessList.append(workerProcessItem)

        return workerProcessList

    # endregion




    #region PULSE SEND OPERATIONS

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
                    return 0

                print('Update successful.')
                return 1

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

    #endregion