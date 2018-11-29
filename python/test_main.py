from main import *
import pytest, requests

# @pytest.fixture
# def testingApp():
#     app = Flask("testing")
#     #ensure using local testing db
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test:password@172.17.0.1:5432/test'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config['MAX_CONTENT_LENGTH'] = 16 * 1024
#     app.secret_key = b'\xc48\xd3!w\xf8U\x06\xc9([\xac\xd9\xfe\xbaj'
#     db.app = app
#     db.init_app(app)
#     # yeild app

def test_generate_test_events():
    rv = generate_test_events(5)
    #check that the rv is a list of 5 Events
    assert (isinstance(rv, list) and len(rv) == 5 and isinstance(rv[0], Event))

def test_event_to_dict():
    l = generate_test_events(1)
    rv = event_to_dict(l[0])
    #check rv is a dict with 10 keys
    assert  (isinstance(rv, dict) and len(rv) == 10)

def test_geocode():
    address = "1585 E 13th Ave Eugene OR 97403"
    rv = geocode(address)
    assert (rv[0] == 44.0459883)

def test_healthcheck():
    rv = requests.get('http://localhost/api/healthcheck').json()
    assert ('sup' in rv['data'])

def test_reset_db():
    rv = requests.get('http://localhost/api/reset_db').json()
    assert ('Success' in rv['message'])

def test_gen_event_endpoint():
    rv = requests.get('http://localhost/api/event/gen_events/5').json()
    assert('success' in rv['message'])

def test_gen_event_campus_endpoint():
    rv = requests.get('http://localhost/api/event/gen_campus_events/5').json()
    assert('success' in rv['message'])

def test_get_event():
    rv = requests.get('http://localhost/api/event/1').json()
    assert('message' not in rv)

def test_get_event_all():
    rv = requests.get('http://localhost/api/event/all').json()
    assert('events' in rv)

def test_insert_event():
    e1 = Event()
    db.session.add(e1)
    rv = db.session.commit()
    assert (rv == None)

def test_add_rating():
    r1 = Review(party_id=1, rating=3)
    db.session.add(r1)
    rv = db.session.commit()
    assert (rv == None)