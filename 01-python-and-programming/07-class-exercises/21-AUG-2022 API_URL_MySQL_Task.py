from flask import Flask, request, jsonify

import mysql.connector as conn

app = Flask(__name__)
mydb = conn.connect(host = "localhost", user = "root", passwd = "Anushka_27")
cursor = mydb.cursor()
# cursor.execute("create database if not exists tasksql")
# cursor.execute("create table tasksql.mysql_table (name varchar(40), number int)")

@app.route('/sql/table', methods = ['GET', 'POST'])
def show_data():
    get_database_name = request.args.get("get_database_name")
    get_table_name = request.args.get("get_table_name")
    cursor.execute(f"select * from {get_database_name}.{get_table_name}")
    l= []
    for i in cursor.fetchall():
            l.append(i)
    return jsonify(str(l))
  
if __name__ == '__main__':
    app.run()


"""Put database name and table name in the url to get the result."""