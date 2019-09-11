import sqlite3 as sql
class DbController:



    def initDb(self):

        CT_Job = "CREATE TABLE IF NOT EXISTS Job (Id NVARCHAR(8), JobOrderNumber INTEGER, Region NVARCHAR(10), IsSended BOOLEAN, CreatedTime datetime, Guid NVARCHAR(36))"
        CT_Worker = "CREATE TABLE IF NOT EXISTS Worker (Id NVARCHAR(8), JobId INTEGER, OperatorId INTEGER, IsSended BOOLEAN, CreatedTime datetime, Guid NVARCHAR(36))"
        CT_WorkerProcess = "CREATE TABLE IF NOT EXISTS WorkerProcess (Id NVARCHAR(8), WorkerId INTEGER, OperatorId INTEGER, ProcessId INTEGER, IsSended BOOLEAN, CreatedTime datetime, Guid NVARCHAR(36))"
        CT_Pulse = "CREATE TABLE IF NOT EXISTS Pulse (Id NVARCHAR(8), JobId INTEGER, IsSended BOOLEAN, CreatedTime datetime, Guid NVARCHAR(36))"
        conn = self.getConnection()

        cmd = conn.cursor()
        cmd.execute(CT_Job)
        cmd.execute(CT_Worker)
        cmd.execute(CT_WorkerProcess)
        cmd.execute(CT_Pulse)
        conn.commit()
        conn.close()
        return "Tables are created."


    def getConnection(self):
        conn = sql.connect("db.sqlite")
        if conn == False:
            print('not connected')
            return None

        return conn
