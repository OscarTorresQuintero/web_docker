from flask import Flask, render_template, request, redirect
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

MYSQL_PASSWORD = "super_secret_123"

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME")
    )

@app.route("/")
def index():
    resultado = 10 / 0
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM aprendices")
    aprendices = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", aprendices=aprendices)

@app.route("/registrar", methods=["POST"])
def registrar():
    nombre = request.form["nombre"]
    documento = request.form["documento"]
    ficha = request.form["ficha"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO aprendices
        (nombre_completo, numero_documento, ficha)
        VALUES (%s,%s,%s)
        """,
        (nombre, documento, ficha),
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True)
