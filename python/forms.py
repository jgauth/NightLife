from wtforms import Form, BooleanField, StringField, validators

# Custom validator checks for inputs containing only whitespace
def noWhiteSpace():
    message = 'Must have valid characters.'

    def _noWhiteSpace(form, field):
        s = field.data.strip()
        if s == '':
            raise validators.ValidationError(message)
        
    return _noWhiteSpace


class NewEventForm(Form):
    name = StringField('Name', [validators.Length(max=255), validators.InputRequired()])
    address = StringField('Address', [validators.Length(max=255), validators.InputRequired()])
    host = StringField('Host', [validators.Length(max=255), validators.InputRequired()])
    theme = StringField('Theme', [validators.Length(max=255)])
    description = StringField('Description', [validators.Length(max=255)])
    time_start = StringField('Start Time', [validators.Length(max=255), validators.InputRequired()])
    time_end = StringField('End Time', [validators.Length(max=255), validators.InputRequired()])

class TestForm(Form):
    name = StringField('Name', [validators.Length(max=255), validators.InputRequired(), noWhiteSpace()])
    address = StringField('Address', [validators.Length(max=255), validators.InputRequired(), noWhiteSpace()])
