from RecordList import RecordList
from User import User
import mysql.connector

class RecordListImplemented(RecordList):
    def __init__(self) -> None:
        try:
            self.mydb = mysql.connector.connect(
                host="localhost", user="root", password="", database="ddrproject")
            self.mycursor = self.mydb.cursor()
        
            self.mycursor.execute("SELECT * FROM records")
        except:
            print('The connection to the Database Server could not be established.\nPlease make sure your Database Server is on, and run the "RecordAdder.py" file again. Database will automatically be created.')
            exit()

    def getUserList(self):
        self.usrList = []
        self.records = self.mycursor.fetchall()
        for record in self.records:
            self.usrList.append(User(record[0], record[1], record[2]))
        return self.usrList