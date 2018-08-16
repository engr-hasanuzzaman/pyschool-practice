from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import DataRequired

class LoginForm(FlaskForm):
  username = StringField('Username', validator=[DataRequired])
  password = PasswordField('Password', validator=[DataRequired])
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Singn In')