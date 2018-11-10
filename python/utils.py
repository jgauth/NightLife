import sys

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
