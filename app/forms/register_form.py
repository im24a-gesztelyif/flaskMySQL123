from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
    username = StringField('Benutzername', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Passwort', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField('Registrieren')
