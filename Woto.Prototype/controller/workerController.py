# -*- coding: utf-8 -*-
import os, sys, inspect



current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from controller.dbController import DbController
from controller.jobController import JobController
from controller.utilController import UtilController as util
class WorkerController:

    def startJob(self, jobOrderNumber, operatorProcessList):
        print(jobOrderNumber, ' - ', operatorProcessList)


    def createWorker(self, jobOrderNumber, operatorList, operatorProcessList):
        # print('--------createWorker bas----')
        # print(str(operatorList))
        if len(operatorList) > 0:
            conn = DbController().getConnection()
            cmd = conn.cursor()
            jobId = JobController().createJob(jobOrderNumber)
            for operatorId in operatorList:
                query_Worker = "INSERT INTO Worker (Id, JobId, OperatorId, IsSended, CreatedTime, Guid) VALUES (?, ?, ?, ?, ?, ?)"
                cmd.execute(query_Worker, (util().getUIID8(), jobId, operatorId, False, util().getNow(), util().getUIID(),))
                workerId = cmd.lastrowid
                for obj in operatorProcessList:
                    if operatorId == obj.operatorCode:
                        query_WorkerProcess = "INSERT INTO WorkerProcess (Id, WorkerId, OperatorId, ProcessId, IsSended, CreatedTime, Guid) VALUES (?, ?, ?, ?, ?, ?, ?)"
                        cmd.execute(query_WorkerProcess, (util().getUIID8(), workerId, obj.operatorCode, obj.processCode, False, util().getNow(), util().getUIID(),))
            conn.commit()
            conn.close()
        return jobId
        # print('--------createWorker bit----')


    def getWorkersForJobOrderNumber(self, jobId):
        # print('-----getWorkersForJobOrderNumber-----' + str(jobId))
        conn = DbController().getConnection()
        cmd = conn.cursor()
        query_getWorkers = "SELECT wp.Id, j.Id, wp.OperatorId, wp.ProcessId, wp.CreatedTime FROM WorkerProcess wp " \
                           "INNER JOIN Worker w ON w.Id = wp.WorkerId " \
                           "INNER JOIN Job j ON j.Id = w.JobId " \
                           "WHERE j.Id = ?"
        return cmd.execute(query_getWorkers, (jobId,))
