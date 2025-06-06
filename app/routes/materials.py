from flask import Blueprint, jsonify
from app.db import get_connection

app = Blueprint('materials', __name__)
#bp = Blueprint('materials', __name__, url_prefix='/materials')

@app.route('/getMaterials', methods=['GET'])
def get_all_materials():
    try:
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Material;")
        materials = cursor.fetchall()
        cursor.close()
        return jsonify(materials), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
