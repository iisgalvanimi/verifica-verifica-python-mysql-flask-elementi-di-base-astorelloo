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
#____________________________________________________________________
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
#____________________________________________________________________
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
#____________________________________________________________________
#punto 4
def deleteInsetti(id):
    query = "DELETE FROM Insetti WHERE id = %s"
    mycursor.execute(query, (id,))
    mydb.commit()
    return mycursor.rowcount

@app.route("/delete/<id>", methods=["DELETE"])
def delete(id):
    rows_deleted = deleteInsetti(id)
    if rows_deleted == 1:
        return jsonify({'message': 'Insetto eliminato con successo'}), 200
    else:
        return jsonify({'message': 'Errore durante l\'eliminazione o ID non trovato'}), 404



#____________________________________________________________________
if __name__ == "__main__":
    app.run()