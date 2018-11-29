import sys, requests
from models import Event
from random import uniform, randint
from datetime import datetime


# Google maps API key
GMAPS_KEY = "AIzaSyDK0VvGmW9rc1y-oX6APE7Rc3wQnoRUI58"

def eprint(*args, **kwargs):
    '''
    Utility for redirecting print IO to console for debugging (bypasses Flask defaults)

    Input/Return: Same as Python print
    Effects: Output to local console
    '''
    print(*args, file=sys.stderr, **kwargs)

def geocode(address):
    '''
    Utility to geocode Google Maps address, uses google maps Geocoding API

    Input:
        Address: String
    Returns:
        Float, tuple of lat(float), lng(float), formatted_address(string)(this has apartment numbers, house numbers, etc removed)
    '''
    address = address.replace(' ', '+').replace('.', '')

    parameters = {'address':address, 'key':GMAPS_KEY}
    try:
        response = requests.get("https://maps.googleapis.com/maps/api/geocode/json", parameters).json()

        lat = response['results'][0]['geometry']['location']['lat']
        lng = response['results'][0]['geometry']['location']['lng']
        formatted_address = response['results'][0]['formatted_address']

        return (lat, lng, formatted_address)

    except requests.exceptions.RequestException as e:
        eprint("Formatting failure")
        pass

def generate_test_events(n):
    '''
    Helper function called by API endpoint to generate test events

    Input:
        n: int, the number of events to generate
    Returns:
        event_list: a list of Event model objects to place on the map
    '''
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
    '''
    Utility to convert an event to a python dictionary.
    Used by the /api/event endpoint

    Input:
        e: Event model object
    Returns:
        item: python dictionary representation of event.
    '''
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