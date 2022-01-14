import mysql.connector
from flask import jsonify
import json

#convert result from sql to json
def to_json(myresult):
  customer_all=[]
  for x in myresult:
    myjson3 = {
                'id': x[0],
                'name': x[1],
                'surname': x[2] 
            }
    customer_all.append(myjson3)
  customer_all_json= f'{{"results": {json.dumps(customer_all)}}}'
  return(jsonify(customer_all_json))

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



def post():
  sql = "INSERT INTO customer (name, surname) VALUES (%s, %s)"
  val = ("Hall", "Highway")
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "record inserted.")

def get():

  print("get:")
  mycursor.execute("SELECT * FROM customer")
  myresult = mycursor.fetchall()
  print(to_json(myresult))

def getLast():

  print("get:")
  mycursor.execute("SELECT * FROM customer ORDER BY customer_id DESC LIMIT 1")
  myresult = mycursor.fetchall()
  print(to_json(myresult))
  

#post()
get()
#getLast()







