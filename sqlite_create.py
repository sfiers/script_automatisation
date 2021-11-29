import sqlite3

connexion = sqlite3.connect("albums2.db")
curseur = connexion.cursor()

sql_table_artiste = """CREATE TABLE artiste (
    artiste_id INTEGER NOT NULL PRIMARY KEY,
    nom VARCHAR);"""

curseur.execute(sql_table_artiste)

sql_table_album = """CREATE TABLE album (
    album_id INTEGER NOT NULL PRIMARY KEY,
    artiste_id INTEGER REFERENCES artiste,
    titre VARCHAR,
    année_sortie INTEGER);"""

curseur.execute(sql_table_album)

curseur.execute('INSERT INTO artiste (nom) VALUES ("Micheal Jackson")');
curseur.execute('INSERT INTO artiste (nom) VALUES ("Céline Dion")');

curseur.execute('INSERT INTO album (artiste_id, titre, année_sortie) values (1, "Thriller", 1983);')
curseur.execute('INSERT INTO album (artiste_id, titre, année_sortie) values (2, "dfsfd", 1993);')
curseur.execute('INSERT INTO album (artiste_id, titre, année_sortie) values (2, "blabla", 1944);')

connexion.commit()
connexion.close()