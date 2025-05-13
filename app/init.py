from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

con=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="hello12345",
    database="taskplaner"
)

@app.route('/getTables',methods=['GET'])
def get_tables():
    try:
        cursor = con.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        cursor.close()

        table_names=[table[0] for table in tables]
        return jsonify({"tables":table_names}),200
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

if __name__ == '__main__':
    print("connecting to DB...")
    app.run(debug=True)
