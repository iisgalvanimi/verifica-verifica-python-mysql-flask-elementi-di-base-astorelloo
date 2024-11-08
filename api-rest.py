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
#___________________________________________________
#punto 6
def updateInsetto(id, data):#(nome, famiglia, habitat, alimentazione, caratteristiche)
    query = "UPDATE Insetti SET nome = %s, famiglia = %s, habitat = %s, alimentazione = %s, caratteristiche = %s WHERE id = %s"
    values = (data['nome'], data['famiglia'], data['habitat'], data['alimentazione'],data['caratteristiche'], id)
    mycursor.execute(query, values)
    mydb.commit()
    return mycursor.rowcount

@app.route("/update/<id>", methods=["PUT"])
def update(id):
    data = request.json
    
    required_fields = ['nome', 'famiglia', 'habitat', 'alimentazione', 'caratteristiche']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Dati mancanti'}), 400

    rows_updated = updateInsetto(id, data)
    if rows_updated == 1:
        return jsonify({'message': 'Insetto aggiornato con successo'}), 200
    else:
        return jsonify({'message': 'Errore'}), 404

#____________________________________________________________________
#punto 7
def getByNome(nome):
    query = "SELECT * FROM Insetti WHERE nome = %s"
    mycursor.execute(query, (nome,))
    rows = mycursor.fetchall()
    return rows
@app.route("/nome/<nome>")
def getInsettoByNome(nome):
    data = getByNome(nome)
    return jsonify({nome: data})
#____________________________________________________________________
if __name__ == "__main__":
    app.run()