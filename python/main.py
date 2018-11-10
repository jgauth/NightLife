import json, os, requests
from utils import eprint, geocode
from flask import Flask, request, redirect, url_for, flash, abort, jsonify
from models import db, Event
from forms import NewEventForm, TestForm
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


@app.route("/api/healthcheck", methods=['GET'])
def healthcheck():
    return jsonify({ 'data': 'sup' })

@app.route("/api/event/create", methods=['POST','PUT'])
def create_event():

    form = TestForm(request.form)

    eprint("method: " + request.method)
    if request.method == 'POST' or request.method == 'PUT':
        if form.validate(): # WTForm validation
            eprint(request.form['name'])
            eprint(request.form['address'])

            #handle db here
            ############# ffffffffinish this
            name = request.form['name']
            address = request.form['address']
            loc_data = geocode(address)
            lat = loc_data[0]
            long = loc_data[1]
            new_event = Event(name=name, geo='POINT({} {})'.format(lat, long), lat=lat, long=long, address=address)

            db.session.add(new_event)
            db.session.commit()

            response = jsonify({ 'message': 'validation/upload success' })
            response.status_code = 200
        else:
            response = jsonify({'message': 'validation failed'})
            response.status_code = 400
        return response
