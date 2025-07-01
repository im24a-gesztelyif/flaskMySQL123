from flask import Blueprint, jsonify
from app.db import get_connection

app = Blueprint('TaskMaterial', __name__)

@app.route('/TaskMaterial', methods=['GET'])
def get_all_materials():
    try:
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM AufgabeMaterial;")
        TaskMat = cursor.fetchall()
        cursor.close()
        return jsonify(TaskMat), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
