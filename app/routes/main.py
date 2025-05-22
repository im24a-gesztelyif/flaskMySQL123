import os
from flask import Blueprint, render_template

app = Blueprint('main', __name__)

@app.route('/')
def index():
    return render_template('index.html')

"""
@app.route('/')
def serve_frontend():
    # Get the directory where this script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up two levels and into frontend/templates
    frontend_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'frontend', 'templates'))
    print(f'Frontend directory is located in: {frontend_path}')
    return send_from_directory(frontend_path, 'index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    static_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'frontend', 'static'))
    return send_from_directory(static_path, filename)
    """