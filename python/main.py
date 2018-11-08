import json, os, requests
from utils import *
from flask import Flask, request, redirect, url_for, flash, abort, jsonify
from models import db, Event
# from flask_migrate import Migrate

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://john:johnpassword@localhost/john' # Uses localhost (cli works, app doesn't)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://john:johnpassword@db/john' # Uses docker container alias (cli doens't work, app does)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://john:johnpassword@172.17.0.1:5432/john' # Uses docker bridge ip (cli and app work)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024
app.secret_key = b'\xc48\xd3!w\xf8U\x06\xc9([\xac\xd9\xfe\xbaj'

GMAPS_KEY = "AIzaSyDK0VvGmW9rc1y-oX6APE7Rc3wQnoRUI58"

db.app = app
db.init_app(app)

def geocode(address):
    '''
    Takes address(string)
    returns tuple of lat(float), lng(float), formatted_address(string)
    note: formatted_address will remove apt #s, room #, etc'''

    # example
    # https://maps.googleapis.com/maps/api/geocode/json?address=1337+Hilyard+St,+Eugene,+OR+97401&key=AIzaSyDK0VvGmW9rc1y-oX6APE7Rc3wQnoRUI58

    # Format address to be url valid
    # may need to adjust formatting to properly handle front-end format
    address = address.replace(' ', '+').replace('.', '')

    parameters = {'address':address, 'key':GMAPS_KEY}
    try:
        response = requests.get("https://maps.googleapis.com/maps/api/geocode/json", parameters).json()

        lat = response['results'][0]['geometry']['location']['lat']
        lng = response['results'][0]['geometry']['location']['lng']
        formatted_address = response['results'][0]['formatted_address']

        return (lat, lng, formatted_address)

    except requests.exceptions.RequestException as e:
        # requests error
        # do something
        pass


@app.route("/api/healthcheck", methods=['GET'])
def healthcheck():
    return jsonify({ 'data': 'sup' })

@app.route("/api/event/create", methods=['POST','PUT'])
def create_event():

    eprint("method: " + request.method)
    eprint("endpoint: " + request.endpoint)
    if request.method == 'POST' or request.method == 'PUT':
        eprint(request.form['name'])

    response = jsonify({ 'message': 'upload success' })
    response.status_code = 200
    return response