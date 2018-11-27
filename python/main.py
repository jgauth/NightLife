import json, os, operator
from utils import *
from flask import Flask, request, redirect, url_for, flash, abort, jsonify
from models import db, Event, Review
from forms import NewEventForm, TestForm
# from flask_migrate import Migrate

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://john:johnpassword@localhost/john' # Uses localhost (cli works, app doesn't)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://john:johnpassword@db/john' # Uses docker container alias (cli doens't work, app does)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://john:johnpassword@172.17.0.1:5432/john' # Uses docker bridge ip (cli and app work)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024
app.secret_key = b'\xc48\xd3!w\xf8U\x06\xc9([\xac\xd9\xfe\xbaj'

db.app = app
db.init_app(app)

def get_rating(party_id):
    result = db.session.query(db.func.avg(Review.rating).label('average')).filter(Review.party_id==party_id)
    return result[0][0]


@app.route("/api/healthcheck", methods=['GET'])
def healthcheck():
    return jsonify({ 'data': 'sup' })

@app.route("/api/reset_db", methods=['GET'])
def reset_db():
    try:
        db.drop_all()
        db.create_all()
        response = jsonify({ 'message': 'Successfully reset db' })
        response.status_code = 200
    except:
        response = jsonify({ 'message': 'Reset db failed check output' })
        response.status_code = 400
    return response

@app.route("/api/event/gen_events/<int:n>", methods=['GET'])
def gen_events(n):
    event_list = generate_test_events(n)
    for e in event_list:
        db.session.add(e)
    db.session.commit()
    response = jsonify({ 'message': 'success' })
    response.status_code = 200
    return response

@app.route("/api/event/<int:id>", methods=['GET'])
def get_event(id):
    event = Event.query.get(id)
    if event is None:
        response = jsonify({'message': 'invalid event ID'})
        response.status_code = 400
        return response

    event_dict = event_to_dict(event)
    event_dict['rating'] = get_rating(id)
    response = jsonify(event_dict)
    response.status_code = 200
    return response


@app.route("/api/event/all", methods=['GET'])
def get_all():
    all_events = Event.query.all()
    json_list = []
    for row in all_events:
        event_dict = event_to_dict(row)

        if get_rating(row.id) == None: event_dict['rating'] = 0
        else: event_dict['rating'] = get_rating(row.id)

        json_list.append(event_dict)

    json_list.sort(key=operator.itemgetter('rating'), reverse=True)

    response = jsonify({'events':json_list})
    response.status_code = 200

    return response

@app.route("/api/event/create", methods=['POST','PUT'])
def create_event():

    form = NewEventForm(request.form)

    if request.method == 'POST' or request.method == 'PUT':

        if form.validate(): # WTForm validation

            eprint("Form successfully validated")

            name = form.eventNameInput.data
            host = form.eventHostInput.data
            theme = form.eventThemeInput.data
            description = form.eventDescriptionInput.data
            time_start = form.eventStartTimeEntry.data
            time_end = form.eventEndTimeEntry.data
            street = form.eventAddressInput.data
            city = form.eventCityInput.data
            state = form.eventStateInput.data
            zip = form.eventZipInput.data
            
            address = "{}, {}, {} {}".format(street, city, state, zip)
            eprint("POST address: " + address)
            geo_tuple = geocode(address)
            eprint(geo_tuple)
            

            #handle db here
            lat = geo_tuple[0]
            lng = geo_tuple[1]
            new_event = Event(name=name, geo='POINT({} {})'.format(lat, lng), lat=lat, lng=lng, address=address, host=host, theme=theme, description=description, time_start=time_start, time_end=time_end)

            db.session.add(new_event)
            db.session.commit()

            response = jsonify({ 'message': 'validation/upload success' })
            response.status_code = 200
            return redirect('/')
        else:
            eprint(form.errors)
            response = jsonify({'validation failed': form.errors})
            response.status_code = 400
        return response

@app.route("/api/event/add_rating", methods=['POST'])
def add_rating():

    rating = request.form['partyRatingSlider']
    eventId = request.form['eventId']

    r1 = Review(party_id=eventId, rating=rating)
    db.session.add(r1)
    db.session.commit()

    response = jsonify({ 'message': 'rating upload success' })
    response.status_code = 200

    return response