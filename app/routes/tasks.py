from flask import Blueprint, jsonify
from app.db import get_connection

bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@bp.route('/all', methods=['GET'])
def get_all_tasks():
    try:
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Aufgabe;")
        tasks = cursor.fetchall()
        cursor.close()
        return jsonify(tasks), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500