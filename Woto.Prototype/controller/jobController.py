# -*- coding: utf-8 -*-
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from controller.dbController import DbController
class JobController:

    def startJob(self, jobOrderNumber, operatorProcessList):
        print(jobOrderNumber, ' - ', operatorProcessList)


    def createJob(self, jobOrderNumber):
        conn = DbController().getConnection()
        cmd = conn.cursor()
        cmd.execute("INSERT INTO Job (JobOrderNumber) VALUES (?)", (jobOrderNumber,))
        conn.commit()
        conn.close()
        return cmd.lastrowid
