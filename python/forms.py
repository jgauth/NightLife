from wtforms import Form, DateTimeField, IntegerField, StringField, validators

# Custom validator checks for inputs containing only whitespace
def noWhiteSpace():
    message = 'Must have valid characters.'

    def _noWhiteSpace(form, field):
        s = field.data.strip()
        if s == '':
            raise validators.ValidationError(message)
        
    return _noWhiteSpace

def startsWithLetter():
    message = 'Must start with a letter.'

    def _startsWithLetter(form, field):
        s = field.data
    if (not isinstance(s, str) or not s[0].isalpha()):
        raise validators.ValidationError(message)
    
    return _startsWithLetter


class NewEventForm(Form):  # YYYY:MM:DD:HH:MM:SS #  %Y:%m:%d:%H:%M:%S
    eventNameInput = StringField('Name', [validators.Length(max=255), validators.InputRequired(), noWhiteSpace()])
    eventHostInput = StringField('Host', [validators.Length(max=255), validators.InputRequired(), noWhiteSpace()])
    eventThemeInput = StringField('Theme', [validators.Length(max=255), noWhiteSpace()])
    eventDescriptionInput = StringField('Description', [validators.Length(max=255), noWhiteSpace()])
    eventStartTimeEntry = DateTimeField('Start Time', [validators.InputRequired()], format='%Y-%m-%dT%H:%M')
    eventEndTimeEntry = DateTimeField('End Time', [validators.InputRequired()], format='%Y-%m-%dT%H:%M')
    eventAddressInput = StringField('Address', [validators.Length(max=255), validators.InputRequired(), noWhiteSpace()])
    eventCityInput = StringField('City', [validators.Length(max=255), validators.InputRequired(), noWhiteSpace()])
    eventStateInput = StringField('State', [validators.Length(max=255), validators.InputRequired(), noWhiteSpace()])
    eventZipInput = IntegerField('Zip', [validators.InputRequired()])

class TestForm(Form):
    name = StringField('Name', [validators.Length(max=255), validators.InputRequired(), noWhiteSpace()])
    address = StringField('Address', [validators.Length(max=255), validators.InputRequired(), noWhiteSpace()])  
