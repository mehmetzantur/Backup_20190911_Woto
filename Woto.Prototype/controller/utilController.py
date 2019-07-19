import datetime, uuid

class UtilController:

    region = 'A-03'

    def getNow(self):
        return datetime.datetime.now()

    def getUIID(self):
        return str(uuid.uuid4())
