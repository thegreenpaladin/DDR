# Lazy Loading Pattern
import os
import psutil
from RecordListProxy import RecordListProxy

#showing memory used by program before the object is created
print("Memory used before using the object:",round(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2, 2), "MiBs")

recordList = RecordListProxy()    # driver code


print('\nFeching user list...\n')
usrList = recordList.getUserList()  # this will load the data from the database

#showing memory used by program after the object is created
print("Memory used after using the object:",round(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2, 2), "MiBs\nBelow are 6 records from the database:\n")

#printing 6 of the objects
for x in range(6):
    print(usrList[x])
