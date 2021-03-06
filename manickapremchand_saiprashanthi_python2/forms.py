from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):

    name = StringField('Name of Puppy:')
    eye_color = StringField('Eye-color:')
    good_catcher = StringField('Is Good-Catcher ? (Y/N):')
    submit = SubmitField('Add Puppy')

class AddOwnerForm(FlaskForm):

    name = StringField('Name of Owner:')
    pup_id = IntegerField("Id of Puppy: ")
    submit = SubmitField('Add Owner')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Puppy to Remove:')
    submit = SubmitField('Remove Puppy')
