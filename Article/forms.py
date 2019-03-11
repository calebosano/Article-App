from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, PasswordField
from wtforms.validators import InputRequired, Email, EqualTo


# Users Login form class
class LoginForm(FlaskForm):
    email = StringField('Email Address', InputRequired(message="Email is required"),
                        Email(message="Invalid email Address"))
    password = PasswordField('Password', InputRequired(message="Password is required"),
                             EqualTo('confirm', message='Passwords must match'))
    confirm = PasswordField('Repeat Password')


# Users Registration form class
class RegistrationForm(FlaskForm):
    first_name = StringField('Firstname', InputRequired(message="Firstname is required"))
    last_name = StringField('Lastname', InputRequired(message="Lastname is required"))
    email = StringField('Email Address', InputRequired(message="Email is required"),
                        Email(message="Invalid email Address"))
    phone = IntegerField('Phone Number:', InputRequired(message="Phone Number is required"))
    password = PasswordField('Password', InputRequired(message="Password is required"))


# Articles form class
class CreateArticleForm(FlaskForm):
    title = StringField('Article Title', InputRequired(message="Article title is required"))
    body = TextAreaField('Article Body',InputRequired(message="Article title is required"))

