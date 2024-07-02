from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired(), Length(max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    repeat_password = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class Editor(FlaskForm):
    name = StringField('Name' )
    lastname = StringField('Lastname' )
    email =  StringField('Email')
    number = StringField("number",validators=[Length(min=9)])
    submit = SubmitField('save change')

class Addproduct(FlaskForm):
    name = StringField("name",validators=[DataRequired()])
    photo = StringField("photo",validators=[DataRequired()])
    submit = SubmitField("Add")    
    
class Deleteproduct(FlaskForm):
    name = StringField("name",validators=[DataRequired()]) 
    submit = SubmitField("delete")   