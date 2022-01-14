from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask import json
import mysql.connector
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
  return(jsonify(customer_all))

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
  print("Create table 'customer' successful")
except:
  print("Table 'customer' already exists")



@app.route('/customer', methods=['GET'])
def get_all_books():
  print("get:")
  mycursor.execute("SELECT * FROM customer")
  myresult = mycursor.fetchall()
  return(to_json(myresult))

@app.route('/customer/<id>', methods=['GET'])
def get_one_customer(id):
  print("get:")
  mycursor.execute(f"SELECT * FROM customer  WHERE customer_id = {id}")
  myresult = mycursor.fetchall()
  return(to_json(myresult))

@app.route('/customer/<id>', methods=['DELETE'])
def delete_one_customer(id):
  print("delete:")
  mycursor.execute(f"DELETE FROM customer WHERE customer_id = {id}")
  return jsonify({'result' : "Successfully deleted"})  

@app.route('/customer/<id>', methods=['PUT'])
def change_one_customer(id):
  print("put:")
  name= request.json['name']
  surname= request.json['surname']  
  sql = f"UPDATE customer SET name = '{name}' , surname = '{surname}' WHERE customer_id = {id}"
  mycursor.execute(sql)
  mydb.commit()



  mycursor.execute(f"SELECT * FROM customer  WHERE customer_id = {id}")
  myresult = mycursor.fetchall()
  return(to_json(myresult))
  

@app.route('/customer', methods=['POST'])
def add_book():
 name= request.json['name']
 surname= request.json['surname']
 sql = "INSERT INTO customer (name, surname) VALUES (%s, %s)"
 val = (name, surname)
 mycursor.execute(sql, val)
 mydb.commit()
 mycursor.execute("SELECT * FROM customer ORDER BY customer_id DESC LIMIT 1")
 myresult = mycursor.fetchall()
 return(to_json(myresult))


 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')
    print("Microservice is ready")
    