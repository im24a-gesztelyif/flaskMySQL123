import os
from flask import Blueprint, send_from_directory

app = Blueprint('main', __name__)

@app.route('/')
def serve_frontend():
    frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'frontend'))
    print(f'Frontend directory is located in: {frontend_path}')
    return send_from_directory(frontend_path, 'index.html')