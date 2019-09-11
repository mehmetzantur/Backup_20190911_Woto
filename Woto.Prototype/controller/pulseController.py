# -*- coding: utf-8 -*-
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from controller.dbController import DbController
from controller.utilController import UtilController as util, Constant as const

class PulseController:

    def createPulse(self, jobId):
        id = util().getUIID8()
        conn = DbController().getConnection()
        cmd = conn.cursor()
        cmd.execute("INSERT INTO Pulse (Id, JobId, IsSended, CreatedTime, Guid) VALUES (?, ?, ?, ?, ?)", (id, jobId, False, util().getNow(), util().getUIID(),))
        conn.commit()
        conn.close()
        return id
