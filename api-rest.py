from flask import Flask, jsonify, request
import mysql.connector
import pymysql

# Connessione a MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Animali"
)
mycursor = mydb.cursor()
app = Flask(__name__)

def getAllData():
    mycursor.execute("SELECT * FROM Insetti")
    rows = mycursor.fetchall()
    result = []
    for x in rows:
        result.append(x)
    return result
@app.route("/")

@app.route("/dati")
def index():
    data = getAllData()
    return jsonify({'Insetti': data})

if __name__ == "__main__":
    app.run()