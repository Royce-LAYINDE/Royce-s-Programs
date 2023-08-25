# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 14:57:12 2023

@author: Royce
"""

import sqlite3

# Chemin vers le fichier de la base de données SQLite
database_file = "C:/Users/lenovo/Documents/DIT-s-projet-22-23/DIT_Projet.db"

try:
    # Créez une connexion à la base de données SQLite
    conn = sqlite3.connect(database_file)

    # Créez un curseur pour exécuter des requêtes
    cursor = conn.cursor()

    # Exécutez une requête SELECT sur la table 'Notes'
    cursor.execute("SELECT * FROM Notes")

    # Récupérez les résultats de la requête
    results = cursor.fetchall()

    # Générer le code HTML pour le tableau
    html_table = "<table border='1'>"
    html_table += "<tr><th>ID</th><th>Prénom</th><th>Nom</th><th>Note devoir anglais</th><th>Note examen anglais</th><th>Note devoir TEC</th><th>Note examen TEC</th><th>Note devoir Python</th><th>Note examen Python</th><th>Note devoir R</th><th>Note examen R</th><th>Note devoir outils stat</th><th>Note examen outils stat</th><th>Note devoir outils math</th><th>Note examen outils math</th><th>Note devoir DevOps</th><th>Note examen DevOps</th><th>Note devoir IoT</th><th>Note examen IoT</th><th>Note devoir outils IA</th><th>Note examen outils IA</th></tr>"
    for row in results:
        html_table += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td><td>{row[5]}</td><td>{row[6]}</td><td>{row[7]}</td><td>{row[8]}</td><td>{row[9]}</td><td>{row[10]}</td><td>{row[11]}</td><td>{row[12]}</td><td>{row[13]}</td><td>{row[14]}</td><td>{row[15]}</td><td>{row[16]}</td><td>{row[17]}</td><td>{row[18]}</td><td>{row[19]}</td><td>{row[20]}</td></tr>"
    html_table += "</table>"

    # Fermez le curseur et la connexion à la base de données
    cursor.close()
    conn.close()

    # Générer la page HTML complète avec le tableau
    html_page = f"<!DOCTYPE html><html><head><title>Tableau des Notes</title></head><body>{html_table}</body></html>"

    # Écrire le contenu dans un fichier HTML
    with open("table_notes.html", "w") as file:
        file.write(html_page)

except sqlite3.Error as e:
    print("La connexion à la base de données a échoué :", e)
