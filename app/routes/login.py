from flask import Blueprint, request, render_template, redirect, session
from app.db import get_connection

app = Blueprint('login', __name__)

@app.route('/', methods=['GET', 'POST'])
def login():
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
