from flask import Blueprint, jsonify
from app.db import get_connection

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/all', methods=['GET'])
def get_all_users():
    try:
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Benutzer;")
        users = cursor.fetchall()
        cursor.close()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
