# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 17:08:08 2023

@author: layin
"""


import sqlite3
con = sqlite3.connect("dicgjhgrnhjgo1.db")
cur = con.cursor()
cur.execute("CREATE TABLE if not exists Etudiant(Nom, Age, Email)")
cur.execute("""
    INSERT INTO Etudiant VALUES
        ('Alice', 32, "hjfkfb@gmail"),
        ('Bob', 33, "hyuefvyuf@gmail"),
        ('Jean', 30, "hghgkfvyuf@gmail")
""")
con.commit()

print("Voici une liste d' options : ")
print( "1-Sélectionner")  
print("2-Insérer")  
print("3- supprimer") 
print("4-modifier")
option=int(input("Choisissez parmis les options précedentes un numéro: "))
def selectioner(name):
    
    cur.execute(f"SELECT * FROM Etudiant  where Nom={name} ")
    return(cur.fetchone())
def inserer(a):
    cur.execute("""
        INSERT INTO Etudiant VALUES
            (?, ?, ?, a),           
    """)
    con.commit()
def supprimer(b):
    cur.execute("""
        DELETE FROM Etudiant where Nom=b
    """)
    con.commit()
def modifier(c,d):
    cur.execute("""
        UPDATE Etudiant
    SET Nom=c where Nom=d           
    """)
    con.commit()
if option==1:
    name=str(input("Quel est le nom de celui dont vous voulez avoir les infos? "))
    print (selectioner(name))

    
elif option ==2:
    name=input("Quel est le nom de celui dont vous voulez insérer les infos? ")
    age=input("Quel est l'age de celui dont vous voulez  insérer les infos? ")
    mail=input("Quel est l'email de celui dont vous voulez  insérer les infos? ")
    a=[name,age,mail]
elif option ==3:
    name=input("Quel est le nom de celui dont vous voulez supprimer les infos? ")
    supprimer(name)
elif option==4:
    name=input("Quel est le nom de celui dont vous voulez modifier les infos? ")
    new_name=input("Quel est le nouveau nom ? ")
    modifier(new_name,name)
    
print(cur.execute("SELECT * FROM Etudiant"))           
                