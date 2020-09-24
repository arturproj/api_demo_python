from flask import Flask, jsonify
import pymongo
import json

app = Flask(__name__)

obj = { "success":True, "data": { "name":"John", "age":30, "city":"New York"} }

@app.route('/', methods=['GET'])
def index():   
    return "Welcome to API Python"

@app.route('/', methods=['POST'])
def create():
    return jsonify(obj)

@app.route('/<id>', methods=['PUT'])
def update(id):
    obj["param"] = id
    return jsonify(obj)

@app.route('/<id>', methods=['DELETE'])
def delete(id):    
    obj["param"] = id
    return jsonify(obj)