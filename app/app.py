from flask import Flask, jsonify
import mysql.connector
import time

app = Flask(__name__)

def connect_db():
    retries = 5
    while retries > 0:
        try:
            connection = mysql.connector.connect(
                host="db",
                user="root",
                password="rootpassword",
                database="testdb"
            )
            return connection
        except mysql.connector.Error as err:
            print(f"❌ Error conectando a MySQL: {err}. Reintentando...")
            retries -= 1
            time.sleep(5)
    return None


@app.route('/')
def index():
    connection = connect_db()
    if connection is None:
        return jsonify({"error": "No se pudo conectar a MySQL después de varios intentos"}), 500

    cursor = connection.cursor()
    cursor.execute("SELECT 'Conexión exitosa con MySQL desde Docker!'")
    result = cursor.fetchone()
    return jsonify({"mensaje": result[0]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
