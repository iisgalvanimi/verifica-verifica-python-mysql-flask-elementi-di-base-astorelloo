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
def home():
    return('verifica')
@app.route("/dati")
def index():
    data = getAllData()
    return jsonify({'Insetti': data})

#punto 3
def addInsetti(data):
    query = "INSERT INTO Insetti (nome, famiglia, habitat, alimentazione, caratteristiche) VALUES (%s, %s, %s, %s, %s)"
    values = (data['nome'], data['famiglia'], data['habitat'], data['alimentazione'],data['caratteristiche'])
    mycursor.execute(query, values)
    mydb.commit()
    return mycursor.rowcount

@app.route("/add", methods=["POST"])
def add():
    data = request.json
    rows_inserted = addInsetti(data)
    if rows_inserted == 1:
        return jsonify({'message': 'Insetto inserito con successo'}), 201
    else:
        return jsonify({'message': 'Errore durante lo svolgimento della operazione'}), 500



if __name__ == "__main__":
    app.run()