from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask import json
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
  host="mysql",
  user="user",
  password="password",
  database="mysql",
  port= 3306
)
mycursor = mydb.cursor()

app = Flask(__name__)

try:
  mycursor.execute("CREATE TABLE customer (customer_id int AUTO_INCREMENT, name VARCHAR(255) NOT NULL , surname VARCHAR(255) NOT NULL, PRIMARY KEY (customer_id))")
except:
  print("Table 'customer' already exists")



@app.route('/customer', methods=['GET'])
def get_all_books():
  mycursor.execute("SELECT * FROM customers")
  myresult = mycursor.fetchall()
  
  str=""

  for x in myresult:
    print(x)
    str+=x

  return x 

 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')
    print("Microservice is ready")
    