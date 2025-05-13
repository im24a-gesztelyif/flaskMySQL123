from flask import Blueprint, jsonify
from app.db import get_connection

app = Blueprint('progress', __name__)

@app.route('getProgress', methods=['GET'])
def get_progress():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Fortschritt')
        cursor.fetchall()
        cursor.close()
        return jsonify(cursor.fetchall()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500