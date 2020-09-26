from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required,Email, EqualTo
from ..models import User
from wtforms import ValidationError

class RegisterationForm(FlaskForm):
    email = StringField('Enter Your email Address', validators= [Required(), Email()])
    username = StringField('Enter your username', validators=[Required()])
    password = PasswordField('Password', validators=[Required(), EqualTo('password_confirm', message='passwords must match')])
    password_confirm = PasswordField('Confirm Passwords', validators=[Required()])
    submit = SubmitField('sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email address')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('The username is already taken')

class LoginForm(FlaskForm):

    email = StringField('Your email Address', validators=[Required(), Email()])
    password = PasswordField('password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('sign in')

    