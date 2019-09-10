class Worker:
    def __init__(self, id=None, jobId=None, operatorId=None, isSended=None, createdTime=None, guid=None):
        self.id = id
        self.jobId = jobId
        self.operatorId = operatorId
        self.isSended = isSended
        self.createdTime = createdTime
        self.guid = guid