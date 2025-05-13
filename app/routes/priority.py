from flask import Blueprint, jsonify
from app.db import get_connection

app = Blueprint('priority', __name__)

@app.route('getPriorities', methods=['GET'])
def get_all_priorities():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Prioritaet')
        cursor.fetchall()
        cursor.close()
        return jsonify(cursor.fetchall()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500