from flask import Flask, request, jsonify

import mysql.connector as conn

app = Flask(__name__)
mydb = conn.connect(host = "localhost", user = "root", passwd = "Anushka_27")
cursor = mydb.cursor()
# cursor.execute("create database if not exists tasksql")
# cursor.execute("create table tasksql.mysql_table (name varchar(40), number int)")

@app.route('/insert', methods = ['GET', 'POST'])
def insert():
    if (request.method == 'POST') : 
        name = request.json['name']
        number = request.json['number']
        cursor.execute("INSERT into tasksql.mysql_table values(%s,%s)",(name,number))
        mydb.commit()
        return jsonify(str("Successfully inserted"))

@app.route('/update', methods = ['GET', 'POST'])
def update():
    if (request.method == 'POST') : 
        get_name = request.json['get_name']
        cursor.execute("update tasksql.mysql_table set number =  1500 where name = %s", (get_name,))
        mydb.commit()
        return jsonify(str("Successfully updated"))

@app.route('/delete', methods = ['GET', 'POST'])
def delete():
    if (request.method == 'POST') : 
        del_name = request.json['del_name']
        cursor.execute("delete from tasksql.mysql_table where name = %s", (del_name,))
        mydb.commit()
        return jsonify(str("Successfully deleted"))

@app.route('/fetch_data', methods = ['GET', 'POST'])
def fetch_data():
    if (request.method == 'POST') : 
        cursor.execute("select * from tasksql.mysql_table")
        l= []
        for i in cursor.fetchall():
            l.append(i)
        return jsonify(str(l))

if __name__ == '__main__':
    app.run()