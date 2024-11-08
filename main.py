import mysql.connector
#Insetti
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS Animali")
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "Animali"#!!!!!
)
mycursor = mydb.cursor()
#creazione tabella mammiferi con controllo se esiste gia' (se c'e' non la crea)
mycursor.execute("CREATE TABLE IF NOT EXISTS Insetti (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, nome VARCHAR(255), famiglia VARCHAR(255), habitat  VARCHAR(255), alimentazione VARCHAR(255), caratteristiche VARCHAR(255))")