from flask import Flask, send_from_directory
from app import create_app

app = create_app()

# Serve the index.html from the frontend folder
@app.route('/')
def serve_frontend():
    return send_from_directory('frontend', 'index.html')

# Serve other static files (like CSS/JS) from the frontend folder
@app.route('/<path:filename>')
def serve_static_files(filename):
    return send_from_directory('frontend', filename)

if __name__ == '__main__':
    app.run(debug=True)