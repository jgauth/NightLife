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
    name = StringField('Name', [validators.Length(max=255), validators.InputRequired(), noWhiteSpace()])
    host = StringField('Host', [validators.Length(max=255), validators.InputRequired(), noWhiteSpace()])
    theme = StringField('Theme', [validators.Length(max=255), noWhiteSpace()])
    description = StringField('Description', [validators.Length(max=255), noWhiteSpace()])
    # time_start = StringField('Start Time', [validators.Length(max=255), validators.InputRequired()])
    # time_end = StringField('End Time', [validators.Length(max=255), validators.InputRequired()])
    time_start = DateTimeField('Start Time', [validators.Length(max=255), validators.InputRequired()], format='%Y:%m:%d:%H:%M:%S')
    time_end = DateTimeField('End Time', [validators.Length(max=255), validators.InputRequired()], format='%Y:%m:%d:%H:%M:%S')
    street = StringField('Street', [validators.Length(max=255), validators.InputRequired(), noWhiteSpace()])
    city = StringField('Name', [validators.Length(max=255), validators.InputRequired(), noWhiteSpace()])
    state = StringField('Name', [validators.Length(max=255), validators.InputRequired(), noWhiteSpace()])
    zip = IntegerField('Name', [validators.Length(max=20), validators.InputRequired(), noWhiteSpace()])
    # address = StringField('Address', [validators.Length(max=255), validators.InputRequired(), noWhiteSpace()])

class TestForm(Form):
    name = StringField('Name', [validators.Length(max=255), validators.InputRequired(), noWhiteSpace()])
    address = StringField('Address', [validators.Length(max=255), validators.InputRequired(), noWhiteSpace()])
