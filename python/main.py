import boto3
import time
import psycopg2
from geoalchemy2 import Geometry
import json
import os
from flask import Flask, request, redirect, url_for, flash, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask("john")
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db'
app.secret_key = 'ASDGBJQWVWEC@$%#%&#WERGAJBEF'

db = db = SQLAlchemy(app)
migrate = Migrate(app, db)

conn_str = "dbname='%s' user='%s' host='%s' password='%s'" % (
    'john', 'john', 'db', 'johnpassword')
# use our connection values to establish a connection
conn = psycopg2.connect(conn_str)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    location = db.Column(Geometry('LINESTRING'))

@app.route("/api/healthcheck", methods=['GET'])
def healthcheck():
    return jsonify({ 'data': 'sup' })

@app.route("/api/event/create", methods=['POST','PUT'])
def create_event():
#{
#  'event_name': 'testEvent',
#  'event_location': {
#    'lat' : 9.6754,
#    'long' : 23.43453
#  }
#}
    print(request.method)
    print(request.endpoint)
    if request.method == 'POST' or request.method == 'PUT':
        data = request.get_json()
        print(data)

    response = jsonify({ 'message': 'upload success' })
    response.status_code = 200
    return response
