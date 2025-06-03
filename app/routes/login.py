from flask import Blueprint, request, render_template, redirect, session
from app.db import get_connection
from app.forms.login_form import LoginForm
from app.forms.register_form import RegisterForm
from werkzeug.security import generate_password_hash

app = Blueprint('login', __name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        con = get_connection()
        cursor = con.cursor(dictionary=True)

        #KEEP "BINARY" -- Enables case sensitivity
        cursor.execute("SELECT * FROM Benutzer WHERE BINARY BenutzerName = %s", (username,))
        user = cursor.fetchone()
        cursor.close()

        # Currently still checking plain-text password
        if user and user['BenutzerPWD'] == password:
            session['user_id'] = user['BenutzerID']
            session['username'] = user['BenutzerName']
            return redirect('/home')
        else:
            return render_template('login.html', form=form, error="Falsche Zugangsdaten")

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        hashed_password = generate_password_hash(password)

        con = get_connection()
        cursor = con.cursor(dictionary=True)

        # Check if username already exists (case-sensitive)
        cursor.execute("SELECT * FROM Benutzer WHERE BINARY BenutzerName = %s", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            cursor.close()
            return render_template('register.html', form=form, error="Benutzername existiert bereits")

        # Insert new user with hashed password
        cursor.execute("INSERT INTO Benutzer (BenutzerName, BenutzerPWD) VALUES (%s, %s)", (username, hashed_password))
        con.commit()
        cursor.close()
        return redirect('/')

    return render_template('register.html', form=form)