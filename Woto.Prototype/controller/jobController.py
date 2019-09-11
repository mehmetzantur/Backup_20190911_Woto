# -*- coding: utf-8 -*-
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from controller.dbController import DbController
from controller.utilController import UtilController as util, Constant as const

class JobController:

    def startJob(self, jobOrderNumber, operatorProcessList):
        print(jobOrderNumber, ' - ', operatorProcessList)


    def createJob(self, jobOrderNumber):
        conn = DbController().getConnection()
        cmd = conn.cursor()
        cmd.execute("INSERT INTO Job (Id, JobOrderNumber, Region, IsSended, CreatedTime, Guid) VALUES (?, ?, ?, ?, ?, ?)", (util.getUIID8(), jobOrderNumber, const.region, False, util().getNow(), util().getUIID(),))
        conn.commit()
        conn.close()
        return cmd.lastrowid
