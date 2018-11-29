'''
models.py

SQL model logic for interfacing with the database
'''

# Geoalchemy and SQLalchemy for PostgresSql modeling
from geoalchemy2 import Geometry
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLalchemy object
db = SQLAlchemy()

class Event(db.Model):
    '''
    SQLAlchemy for event (party)

    Columns are listed below, with foreign key connection to Review model
    '''
    id = db.Column(db.Integer, primary_key=True)                     #Event ID
    name = db.Column(db.String(255))                                 #Name of Event
    geo = db.Column(Geometry('POINT'))                               #PostGIS Geometry
    lat = db.Column(db.Float)                                        #Latitude
    lng = db.Column(db.Float)                                        #Longitude
    address = db.Column(db.String(255))                              #Physical address (eg. 123 Nowhere lane...)
    host = db.Column(db.String(255))                                 #Event host
    theme = db.Column(db.String(255))                                #Event theme
    description = db.Column(db.String(255))                          #Event description
    time_start = db.Column(db.DateTime)                              #Event start time
    time_end = db.Column(db.DateTime)                                #Event end time
    reviews = db.relationship('Review', backref='event', lazy=True)  #Reviews foreign key

class Review(db.Model):
    '''
    SQLAlchemy for review

    Each object represents a submitted review for a given event.
    '''
    id = db.Column(db.Integer, primary_key=True)                                 #Review ID
    party_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)  #Event ID (foreign key to Event)
    rating = db.Column(db.Float)                                                 #Review rating
