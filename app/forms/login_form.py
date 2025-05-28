from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('BenutzerName', validators=[DataRequired()])
    password = PasswordField('BenutzerPWD', validators=[DataRequired()])
    submit = SubmitField('Login')
