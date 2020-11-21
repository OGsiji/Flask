from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    
    name = StringField('Name of Puppy')
    submit = SubmitField('Add Puppy')
    

class DelForm(FlaskForm):
    
    id = IntegerField('Id number of Puppy to remove: ')
    submit = SubmitField('Remove Puppy')
    
class OwnerForm(FlaskForm):
    
    name = StringField('Name of Owner: ')
    pup_id = IntegerField('Id of Puppy: ')
    submit = SubmitField('Add Owner')