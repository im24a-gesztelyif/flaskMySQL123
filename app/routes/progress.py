from flask import Blueprint, jsonify
from app.db import get_connection

app = Blueprint('progress', __name__)


@app.route('/getProgress', methods=['GET'])
def get_progress():
    try:
        con = get_connection()
        cursor = con.cursor()
        cursor.execute('SELECT * FROM Fortschritt')
        progress = cursor.fetchall()
        cursor.close()
        return jsonify(progress), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500