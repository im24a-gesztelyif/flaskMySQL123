from flask import Blueprint, render_template, session, redirect
from app.db import get_connection

app = Blueprint('main', __name__)

@app.route('/home')
def index():
    if 'user_id' not in session:
        return redirect('/')
    
    con = get_connection()
    cursor = con.cursor(dictionary=True)

    cursor.execute('SELECT * FROM Kategorie WHERE IstAktiv = 1')
    kategorien = cursor.fetchall()

    cursor.execute('SELECT * FROM Prioritaet')
    prioritaeten = cursor.fetchall()

    cursor.execute('SELECT * FROM Fortschritt')
    fortschritte = cursor.fetchall()

    return render_template('index.html',
        kategorien=kategorien,
        prioritaeten=prioritaeten,
        fortschritte=fortschritte,
        username=session['username']
    )