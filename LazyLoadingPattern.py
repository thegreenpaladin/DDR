# Lazy Loading Pattern

import os
import psutil
from RecordListProxy import RecordListProxy

recordList = RecordListProxy()

# memory used by program before the objects are created
print("\nMemory used before loading the objects:", round(
    psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2, 2), "MiBs")

print('\nFetching user list...\n')
# this will load the records from the database as list of objects
usrList = recordList.getUserList()

# showing memory used by program after the objects are created
print("Memory used after loading the objects:", round(
    psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2, 2), "MiBs\n")

# printing 6 objects from the list
print("Below are 6 records from the database:\n")
for x in range(6):
    print(usrList[x])