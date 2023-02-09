
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, Booleanfield
from wtforms.validators import DataRequired

class LoginFor(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = Booleanfield('remember_me')