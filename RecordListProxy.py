from RecordList import RecordList
from RecordListImplemented import RecordListImplemented
class RecordListProxy(RecordList):
    def __init__(self):
        self.recordList = None

    def getUserList(self):
        if self.recordList == None:
            self.recordList = RecordListImplemented()
        return self.recordList.getUserList()