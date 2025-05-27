from flask import Blueprint, jsonify, request
from app.db import get_connection

app = Blueprint('tasks', __name__)

# GET all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        con = get_connection()
        cursor = con.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Aufgabe")
        tasks = cursor.fetchall()
        cursor.close()
        return jsonify(tasks), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST create a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    print("Received task:", data)
    try:
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("""
            INSERT INTO Aufgabe (
                Titel, Beginn, Ende, Ort, Koordinaten, Notiz,
                KategorieID, PrioritaetID, FortschrittID, BenutzerID
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            data['titel'],
            data['beginn'],
            data.get('ende'),
            data.get('ort'),
            data.get('koordinaten'),
            data.get('notiz'),
            data['kategorie_id'],
            data['prioritaet_id'],
            data['fortschritt_id'],
            data['benutzer_id']
        ))
        con.commit()
        cursor.close()
        return jsonify({"message": "Task added"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE a task
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    try:
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("DELETE FROM Aufgabe WHERE AufgabeID = %s", (id,))
        con.commit()
        cursor.close()
        return jsonify({"message": "Task deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# PUT update a task
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    try:
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("""
            UPDATE Aufgabe
            SET Titel = %s,
                Beginn = %s,
                Ende = %s,
                Ort = %s,
                Koordinaten = %s,
                Notiz = %s,
                KategorieID = %s,
                PrioritaetID = %s,
                FortschrittID = %s,
                BenutzerID = %s
            WHERE AufgabeID = %s
        """, (
            data['titel'],
            data['beginn'],
            data.get('ende'),
            data.get('ort'),
            data.get('koordinaten'),
            data.get('notiz'),
            data['kategorie_id'],
            data['prioritaet_id'],
            data['fortschritt_id'],
            data['benutzer_id'],
            id
        ))
        con.commit()
        cursor.close()
        return jsonify({"message": "Task updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
