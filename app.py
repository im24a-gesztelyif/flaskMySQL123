from flask import send_from_directory
from app import create_app

app = create_app()

if __name__ == '__main__':
    print("Starting Flask app...")
    print("Flask Server is running on app.py")
    app.run(debug=True)