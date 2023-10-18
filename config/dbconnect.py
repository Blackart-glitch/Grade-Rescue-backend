import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="grade_rescue"
)

mycursor = mydb.cursor()

