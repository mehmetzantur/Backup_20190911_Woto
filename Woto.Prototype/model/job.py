class Job:
    def __init__(self, id = None, jobOrderNumber=None, region=None, isSended=None, createdTime=None, guid=None):
        self.id = id
        self.jobOrderNumber = jobOrderNumber
        self.region = region
        self.isSended = isSended
        self.createdTime = createdTime
        self.guid = guid