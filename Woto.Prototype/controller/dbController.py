import sqlite3 as sql
class DbController:



    def initDb(self):

        CT_Job = "CREATE TABLE IF NOT EXISTS Job (Id INTEGER PRIMARY KEY, JobOrderNumber)"
        CT_Worker = "CREATE TABLE IF NOT EXISTS Worker (Id INTEGER PRIMARY KEY, JobId INTEGER, OperatorId INTEGER)"
        CT_WorkerProcess = "CREATE TABLE IF NOT EXISTS WorkerProcess (Id INTEGER PRIMARY KEY, WorkerId INTEGER, OperatorId INTEGER, ProcessId INTEGER)"
        conn = self.getConnection()

        cmd = conn.cursor()
        cmd.execute(CT_Job)
        cmd.execute(CT_Worker)
        cmd.execute(CT_WorkerProcess)
        conn.commit()
        conn.close()


    def getConnection(self):
        conn = sql.connect("..\\db.sqlite")
        if conn == False:
            print('not connected')
            return None

        return conn
