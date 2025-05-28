from flask import Blueprint, render_template, session, redirect

app = Blueprint('main', __name__)

@app.route('/home')
def index():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('index.html', username=session['username'])