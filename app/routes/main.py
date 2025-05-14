from flask import Blueprint, send_from_directory

app = Blueprint('main', __name__)

@app.route('/')
def serve_frontend():
    return send_from_directory('frontend', 'index.html')