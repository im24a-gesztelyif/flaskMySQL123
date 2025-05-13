from flask import Blueprint, jsonify
from app.db import get_connection

app = Blueprint('priority', __name__)


@app.route('/getPriorities', methods=['GET'])
def get_all_priorities():
    try:
        con = get_connection()
        cursor = con.cursor()
        cursor.execute('SELECT * FROM Prioritaet')
        priority = cursor.fetchall()
        cursor.close()
        return jsonify(priority), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500