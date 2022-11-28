# Lazy Loading Pattern
import mysql.connector

class RecordList:
    def getUserList(self):
        pass


class RecordListImplemented(RecordList):
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(host="localhost",user="root",password="",database="ddrproject")
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("SELECT * FROM records")

    def getUserList(self):
        self.usrList = []
        self.records = self.mycursor.fetchall()
        for record in self.records:
            self.usrList.append(User(record[0], record[1], record[2]))
        return self.usrList
        

class RecordListProxy(RecordList):
    def __init__(self):
        self.recordList = None

    def getUserList(self):
        if self.recordList == None:
            self.recordList = RecordListImplemented()
        return self.recordList.getUserList()


class User:
    def __init__(self, uid, name, age):
        self.id = uid
        self.name = name
        self.age = age
    
    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getAge(self):
        return self.age
    
    def __str__(self):
        return f"ID: {self.id} | Name: {self.name}\t | Age: {self.age}"


# driver code
recordList = RecordListProxy()

print('\nFeching user list...\n')
usrList = recordList.getUserList() # this will load the data from the database
for usr in usrList:
    print(usr)