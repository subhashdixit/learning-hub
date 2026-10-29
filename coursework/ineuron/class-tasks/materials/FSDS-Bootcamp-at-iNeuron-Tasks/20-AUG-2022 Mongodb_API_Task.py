import collections
import json
from flask import Flask, request, jsonify

import pymongo

app =Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://subhashdixit17:Anushka27@cluster0.elq8eyt.mongodb.net/?retryWrites=true&w=majority")
database = client['taskdb']
collection = database['taskcollection']

@app.route('/insert/mongo', methods = ['GET', 'POST'])
def insert() :
    if (request.method =='POST') :
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name:number})
        return jsonify(str("Successfully inserted"))

@app.route('/update/mongo', methods = ['GET', 'POST'])
def update() :
    if (request.method =='POST') :
        get_name = request.json['get_name']
        collection.update_one({},{"$set": {"get_name" : 100}})
        return jsonify(str("Successfully updated"))

@app.route('/delete/mongo', methods = ['GET', 'POST'])
def delete() :
    if (request.method =='POST') :
        del_name = request.json['del_name']
        del_number =  request.json['del_number']
        collection.delete_one({del_name:del_number})
        return jsonify(str("Successfully deleted"))

@app.route('/fetch_data/mongo', methods = ['GET', 'POST'])
def fetch_date() :
    if (request.method =='POST') :
        # get_name = request.json['get_name']
        l = []
        data = collection.find()
        for i in data :
            l.append(i)
        return jsonify(str(l))

if __name__ == '__main__' :
    app.run()

"""We can change port number if inernal server will occure while connecting postman to local system"""