# -*- coding: utf-8 -*-
import os, sys, inspect



current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from controller.dbController import DbController
from controller.jobController import JobController
class WorkerController:

    def startJob(self, jobOrderNumber, operatorProcessList):
        print(jobOrderNumber, ' - ', operatorProcessList)


    def createWorker(self, jobOrderNumber, operatorList, operatorProcessList):
        conn = DbController().getConnection()
        cmd = conn.cursor()
        jobId = JobController().createJob(jobOrderNumber)
        for operatorId in operatorList:
            cmd.execute("INSERT INTO Worker (JobId, OperatorId) VALUES (?, ?)", (jobId, operatorId,))
            workerId = cmd.lastrowid
            for obj in operatorProcessList:
                if operatorId == obj.operatorCode:
                    cmd.execute("INSERT INTO WorkerProcess (WorkerId, OperatorId, ProcessId) VALUES (?, ?, ?)", (workerId, obj.operatorCode, obj.processCode, ))
        conn.commit()
        conn.close()

