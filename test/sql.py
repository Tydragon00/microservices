import mysql.connector
import json

#convert result from sql to json
def to_json(myresult):
  id = myresult[0][0]
  name = myresult[0][1]
  surname = myresult[0][2]
  x =  f'{{"id": {id}, "name": {name}, "surname": {surname}}}'
  return x 

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password="password",
  database="mysql"
)

mycursor = mydb.cursor()
try:
  mycursor.execute("CREATE TABLE customer (customer_id int AUTO_INCREMENT, name VARCHAR(255) NOT NULL , surname VARCHAR(255) NOT NULL, PRIMARY KEY (customer_id))")
except:
  print("Table 'customer' already exists")



sql = "INSERT INTO customer (name, surname) VALUES (%s, %s)"
val = ("John", "Highway")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


