'''
forms.py

Validate event forms using WTForm validation.
'''

from wtforms import Form, DateTimeField, IntegerField, StringField, validators


def noWhiteSpace():
    '''
    Validates form fields to check for pure whitespace for database integrity.
    
    Input:
        HTML Form Data
    Returns:
        - None [if form validated]
        - Validation Error [if form invalidated]
    '''
    message = 'Must have valid characters.'

    def _noWhiteSpace(form, field):
        '''
        Helper function to check for pure whitespace.

        Raises Validation Error
        '''
        s = field.data.strip()
        if s == '':
            raise validators.ValidationError(message)
        
    return _noWhiteSpace

def startsWithLetter():
    '''
    Input:
        HTML Form Data
    Returns:
        - None [if form validated]
        - Validation Error [if form invalidated]
    '''
    message = 'Must start with a letter.'

    def _startsWithLetter(form, field):
        s = field.data
    if (not isinstance(s, str) or not s[0].isalpha()):
        raise validators.ValidationError(message)
    
    return _startsWithLetter


class NewEventForm(Form):
    '''
    Validates form field input for each of the input fields, using WT validators and custom validators

    Input:
        HTML Form
    Effects:
        Form validation (returns validation error to user-side)
    '''
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
