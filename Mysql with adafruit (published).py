#Some variables might need to be changed depending on how you've set up the database

import mysql.connector
import datetime

mydb = mysql.connector.connect(
host="x",
user="x",
password="x",
database="x" 
)

mycursor = mydb.cursor()

print("Connected..")

sql = "INSERT INTO sensor(verdi,tid) VALUES (%s,%s)"

verdi = 2.0  # Value that gets sent to the database
tid = datetime.datetime.now() # Time sent to the database

val = (verdi, tid)

print("Executing...")

mycursor.execute(sql, val)
mydb.commit()

print("Done")