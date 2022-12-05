import mysql.connector
import random
import string

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="ddrproject")
mycursor = mydb.cursor()

for x in range(100000):
    mycursor.execute("INSERT INTO records (name, nationality, createddate) VALUES ('" +
                     ''.join(random.choices(string.ascii_lowercase, k=20))+"', 'Pakistani',NOW())")
mydb.commit()
mycursor.execute("SELECT * FROM records")
records = mycursor.fetchall()
for record in records:
    print(record[0], ",", record[1], ",", record[2])
 