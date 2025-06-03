from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    username = StringField('Benutzername', validators=[InputRequired(), Length(min=3, max=20)])
    password = PasswordField('Passwort', validators=[InputRequired(), Length(min=4)])
    submit = SubmitField('Registrieren')
