import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="mysql",
  password="mysql"
)

mycursor = mydb.cursor()