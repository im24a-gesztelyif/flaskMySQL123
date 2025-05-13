from flask import Blueprint, jsonify
from app.db import get_connection

app = Blueprint('category', __name__, url_prefix='/category')

@app.route('/getCategories', methods=['GET'])
def get_all_categories():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Kategorie')
        categories = cursor.fetchall()
        cursor.close()
        return jsonify(categories), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
