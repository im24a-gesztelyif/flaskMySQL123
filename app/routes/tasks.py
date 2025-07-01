from flask import Blueprint, jsonify, request, session
from app.db import get_connection

app = Blueprint('tasks', __name__)

# GET all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    if 'user_id' not in session:
        return jsonify({"error": "User not logged in"}), 401

    try:
        con = get_connection()
        cursor = con.cursor(dictionary=True)
        user_id = session.get('user_id')
        cursor.execute("""
                    SELECT 
                        a.AufgabeID,
                        a.Titel,
                        a.Beginn,
                        a.Ende,
                        a.Ort,
                        a.Koordinaten,
                        a.Notiz,
                        a.KategorieID,
                        k.Kategorie AS Kategorie,
                        a.PrioritaetID,
                        p.Prioritaet AS Prioritaet,
                        a.FortschrittID,
                        f.Fortschritt AS Fortschritt
                    FROM Aufgabe a
                    JOIN Kategorie k ON a.KategorieID = k.KategorieID
                    JOIN Prioritaet p ON a.PrioritaetID = p.PrioritaetID
                    JOIN Fortschritt f ON a.FortschrittID = f.FortschrittID
                    WHERE BenutzerID = %s
                       """, (user_id,))
        tasks = cursor.fetchall()
        cursor.close()
        return jsonify(tasks), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST create a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    if 'user_id' not in session:
        return jsonify({"error": "User not logged in"}), 401

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
            data.get('ende') or None,
            data.get('ort') or None,
            data.get('koordinaten') or None,
            data.get('notiz') or None,
            data['kategorie_id'],
            data['prioritaet_id'],
            data['fortschritt_id'],
            session['user_id'] # automatically taken from the session
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
        cursor.execute("SELECT * FROM Aufgabe WHERE AufgabeID = %s AND BenutzerID = %s", (id, session['user_id']))
        task = cursor.fetchone()
        if not task:
            return "Unauthorized", 403
        
        cursor.execute("DELETE FROM Aufgabe WHERE AufgabeID = %s AND BenutzerID = %s", (id, session['user_id']))
        con.commit()
        cursor.close()
        return jsonify({"message": "Task deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# PUT update a task
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    benutzer_id = session['user_id']
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
            WHERE AufgabeID = %s AND BenutzerID = %s
        """, (
            data['titel'],
            data['beginn'],
            data.get('ende') or None,
            data.get('ort') or None,
            data.get('koordinaten') or None,
            data.get('notiz') or None,
            data['kategorie_id'],
            data['prioritaet_id'],
            data['fortschritt_id'],
            benutzer_id,
            id,
            benutzer_id # automatically taken from the session
        ))
        con.commit()
        cursor.close()
        return jsonify({"message": "Task updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
