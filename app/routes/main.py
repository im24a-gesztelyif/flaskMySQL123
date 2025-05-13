from flask import Blueprint

app = Blueprint('main', __name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'Taskplaner API Home'