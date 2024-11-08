import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "Animali"
)
mycursor = mydb.cursor()
sql = "INSERT INTO Insetti (nome, famiglia, habitat , alimentazione, caratteristiche) VALUES ( %s, %s, %s, %s,%s)"
insetti = [
    ("Ape", "Apidae", "Giardini, campi, boschi", "Nettare, polline", "Corpo peloso, ali trasparenti, produce miele"),
    ("Farfallo", "Nymphalidae", "Fiori, prati, boschi", "Nettare", "Ali colorate, trasformazione da crisalide"),
    ("Cimice", "Pentatomidae", "Giardini, campi, case", "Sangue vegetale (succhia il succo delle piante)", "Corpo appiattito, antenne lunghe, pungiglione"),
    ("Mosca", "Muscidae", "Ambienti urbani, case, fiori", "Decomposizione di materiali organici", "Ali trasparenti, corpo piccolo e robusto, occhi grandi"),
    ("Grillo", "Gryllidae", "Prati, giardini, campi", "Erba, foglie, detriti", "Corpo snodato, ali che emettono suoni (canto)"),
    ("Scarafaggio", "Blattidae", "Case, cucine, ambienti umidi", "Detriti, cibo in decomposizione", "Corpo piatto, antenne lunghe, velocità di movimento elevata"),
    ("Libellula", "Libellulidae", "Zone acquatiche, laghi, stagni", "Insetti volanti (cacciati in volo)", "Ali trasparenti, corpo allungato, volo acrobatico"),
    ("Zanzara", "Culicidae", "Ambienti umidi, vicino a stagni e corsi d'acqua", "Sangue di animali e umani (femmine), nettare (maschi)", "Antenne lunghe, pungiglione, volo silenzioso"),
    ("Cavalletta", "Acrididae", "Prati, campi, pascoli", "Erba, piante", "Corpo robusto, lunghe zampe posteriori, salta a grandi distanze"),
    ("Termite", "Termitidae", "Legno, terreni umidi", "Cellulosa (mangiano legno)", "Corpo bianco o giallo pallido, antenne dritte, struttura sociale complessa")
]
mycursor.executemany(sql, insetti)
print(mycursor.rowcount, "i record sono stati inseriti")
# Conferma le modifiche al database
mydb.commit()