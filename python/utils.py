import sys, requests
from models import Event
from random import uniform, randint
from datetime import datetime

GMAPS_KEY = "AIzaSyDK0VvGmW9rc1y-oX6APE7Rc3wQnoRUI58"

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

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

def generate_test_events(n):
    """Generate a list of length n of Event objects"""
    letters = "ABCDEF"
    event_list = []
    for i in range(n):
        name = "Event #{}".format(i)
        host = "Host #{}".format(i)
        theme = letters[i % 6]
        lat = uniform(43.9887109, 44.13261989999999)
        lng = uniform(-123.208402, -123.036699)
        geo = 'POINT({} {})'.format(lat, lng)
        address = "Test 123 Lane, Eugene OR 99999"
        description = "Test description Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut"
        # time_start = "2018-{}-{} {}:{}:00".format(randint(1,12), randint(1,28), randint(0, 23), randint(0, 59))
        # time_end = "2018-{}-{} {}:{}:00".format(randint(1,12), randint(1,28), randint(0, 23), randint(0, 59))
        time_start = datetime.now()
        time_end = datetime.now()
        e = Event(name=name, geo=geo, lat=lat, lng=lng, address=address, host=host, theme=theme, description=description, time_start=time_start, time_end=time_end)
        event_list.append(e)
    return event_list

def generate_campus_test_events(n):
    """Generates a list of length n of Event objects in the UO campus area"""
    letters = "ABCDEF"
    event_list = []
    for i in range(n):
        name = "Event #{}".format(i)
        host = "Host #{}".format(i)
        theme = letters[i % 6]
        lat = uniform(44.049767, 44.039834)
        lng = uniform(-123.083650, -123.064724)
        geo = 'POINT({} {})'.format(lat, lng)
        address = "Test 123 Lane, Eugene OR 99999"
        description = "Test description Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut"
        # time_start = "2018-{}-{} {}:{}:00".format(randint(1,12), randint(1,28), randint(0, 23), randint(0, 59))
        # time_end = "2018-{}-{} {}:{}:00".format(randint(1,12), randint(1,28), randint(0, 23), randint(0, 59))
        time_start = datetime.now()
        time_end = datetime.now()
        e = Event(name=name, geo=geo, lat=lat, lng=lng, address=address, host=host, theme=theme, description=description, time_start=time_start, time_end=time_end)
        event_list.append(e)
    return event_list

def event_to_dict(e):
    item = {}
    item['id'] = e.id
    item['name'] = e.name
    item['lat'] = e.lat
    item['lng'] = e.lng
    item['address'] = e.address
    item['host'] = e.host
    item['theme'] = e.theme
    item['description'] = e.description
    item['time_start'] = e.time_start
    item['time_end'] = e.time_end
    return item