from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask import json
import mysql.connector
import json
from datetime import datetime

#convert result from sql to json
def to_json(myresult):
  customer_all=[]
  for x in myresult:
    myjson3 = {
                'borrowing_id': x[0],
                'book_id': x[1],
                'customer_id': x[2] ,
                'start_date': str(x[3])                
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
  mycursor.execute("CREATE TABLE borrowing (borrowing_id int AUTO_INCREMENT, book_id VARCHAR(255) NOT NULL , customer_id VARCHAR(255) NOT NULL, start_date DATETIME, PRIMARY KEY (borrowing_id))")
  print("Create table 'borrowing' successful")
except:
  print("Table 'borrowing' already exists")


@app.route('/borrowing', methods=['GET'])
def get_all_borrowing():
  print("get:")
  mycursor.execute("SELECT * FROM borrowing")
  myresult = mycursor.fetchall()
  return(to_json(myresult))

@app.route('/borrowing/<id>', methods=['GET'])
def get_one_borrowing(id):
  print("get:")
  mycursor.execute(f"SELECT * FROM borrowing  WHERE borrowing_id = {id}")
  myresult = mycursor.fetchall()
  return(to_json(myresult))

@app.route('/borrowing/<id>', methods=['DELETE'])
def delete_one_borrowing(id):
  print("delete:")
  mycursor.execute(f"DELETE FROM borrowing WHERE borrowing_id = {id}")
  return jsonify({'result' : "Successfully deleted"})  

@app.route('/borrowing/<id>', methods=['PUT'])
def change_one_borrowing(id):
  print("put:")
  book_id= request.json['book_id']
  customer_id= request.json['customer_id']  
  sql = f"UPDATE borrowing SET book_id = '{book_id}' , customer_id = '{customer_id}' WHERE borrowing_id = {id}"
  mycursor.execute(sql)
  mydb.commit()



  mycursor.execute(f"SELECT * FROM borrowing  WHERE borrowing_id = {id}")
  myresult = mycursor.fetchall()
  return(to_json(myresult))
  

@app.route('/borrowing', methods=['POST'])
def add_borrowing():
 book_id= request.json['book_id']
 customer_id= request.json['customer_id'] 
 now = datetime.now()
 formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
 sql = "INSERT INTO borrowing (book_id, customer_id, start_date) VALUES (%s, %s, %s)"
 val = (book_id, customer_id, formatted_date)
 mycursor.execute(sql, val)
 mydb.commit()
 mycursor.execute("SELECT * FROM borrowing ORDER BY borrowing_id DESC LIMIT 1")
 myresult = mycursor.fetchall()
 return(to_json(myresult))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5002')
    print("Microservice is ready")
    