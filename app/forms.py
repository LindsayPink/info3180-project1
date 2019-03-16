from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Email

class User(FlaskForm):
    firstname = StringField('First Name', validators=[InputRequired()])
    lastname = StringField('Last Name', validators=[InputRequired()])
    
    gender = SelectField(u'Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[InputRequired()])
     
    email = StringField('Email', validators=[InputRequired(), Email(message="That's not an email address")])
    location = StringField('Location', validators=[InputRequired()])
    
    bio = TextAreaField('Biography', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], message="That's not a photo")])