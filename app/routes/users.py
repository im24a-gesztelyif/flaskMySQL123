from flask import Blueprint, jsonify
from app.db import get_connection

app = Blueprint('users', __name__)

@app.route('/getUsers', methods=['GET'])
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
