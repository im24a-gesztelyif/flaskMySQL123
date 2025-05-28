from flask import Blueprint, request, render_template, redirect, session
from app.db import get_connection
from app.forms.login_form import LoginForm
from werkzeug.security import check_password_hash

app = Blueprint('login', __name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        con = get_connection()
        cursor = con.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Benutzer WHERE BINARY BenutzerName = %s", (username,))
        user = cursor.fetchone()
        cursor.close()

        if user and check_password_hash(user['BenutzerPWD'], password):
            session['user_id'] = user['BenutzerID']
            session['username'] = user['BenutzerName']
            return redirect('/home')
        else:
            return render_template('login.html', form=form, error="Falsche Zugangsdaten")

    return render_template('login.html', form=form)
    
    """
    if request.method == 'POST':
        username = request.form['BenutzerName']
        password = request.form['BenutzerPWD']

        try:
            con = get_connection()
            cursor = con.cursor(dictionary=True)
            cursor.execute(
                    "SELECT * FROM Benutzer WHERE BINARY BenutzerName = %s AND BINARY BenutzerPWD = %s",
                    (username, password)
            )
            user = cursor.fetchone()
            cursor.close()

            if user:
                session['user_id'] = user['BenutzerID']
                session['username'] = user['BenutzerName']
                return redirect('/home')  # replace with your main route
            else:
                return render_template('login.html', error="Benutzername oder Passwort falsch!")

        except Exception as e:
            return render_template('login.html', error=str(e))

    return render_template('login.html')
    """
