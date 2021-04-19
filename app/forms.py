from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, InputRequired, ValidationError, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired("Please enter a username")])
    password = PasswordField('Password', validators=[InputRequired("Please enter the password")])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired("Please enter a username")])
    email = StringField('Email', validators=[InputRequired("Please enter your email"), Email()])
    password = PasswordField('Password', validators=[InputRequired("Please select a password")])
    password2 = PasswordField('Repeat Password', validators=[InputRequired("Please retype the password"), EqualTo('password', message='Both passwords must match')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Username already taken")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("This email is already registered")