from flask import Blueprint, jsonify
from app.db import get_connection

app = Blueprint('files', __name__)

@app.route('/getFiles', methods=['GET'])
def get_all_materials():
    try:
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Datei;")
        files = cursor.fetchall()
        cursor.close()
        return jsonify(files), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
