import mysql.connector
import random
import string

mydb = mysql.connector.connect(host="localhost", user="root", password="")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS ddrproject")
mycursor.execute("USE ddrproject")
mycursor.execute("CREATE TABLE records (name VARCHAR(255), nationality VARCHAR(255), dob VARCHAR(255))")

for x in range(100000):
    mycursor.execute("INSERT INTO records (name, nationality, dob) VALUES ('" +
                     ''.join(random.choices(string.ascii_lowercase, k=8))+"', 'Pakistani', NOW())")

mydb.commit()