from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host="servidor-bd",
        user="root",
        password="123456",
        database="adso_db"
    )

@app.route("/")
def index():
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
    app.run(host="0.0.0.0", port=5050)
o

