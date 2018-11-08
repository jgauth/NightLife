from geoalchemy2 import Geometry
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))        #Name of Event
    geo = db.Column(Geometry('POINT'))      #PostGIS Geometry
    lat = db.Column(db.Float)               #Latitude
    long = db.Column(db.Float)              #Longitude
    address = db.Column(db.String(255))     #Physical address (eg. 123 Nowhere lane...)
    host = db.Column(db.String(255))        #Event host
    theme = db.Column(db.String(255))       #Event theme
    description = db.Column(db.String(255)) #Event description
    time_start = db.Column(db.DateTime)     #Event start time
    time_end = db.Column(db.DateTime)       #Event end time
