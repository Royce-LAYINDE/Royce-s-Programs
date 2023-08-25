# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 00:26:06 2023

@author: Royce
"""

def trouver_longueur_dernier_mot(phrase, nom_fichier):
    mots = phrase.split()
    
    if len(mots) > 0:
        dernier_mot = mots[-1]
        longueur_dernier_mot = len(dernier_mot)
    else:
        longueur_dernier_mot = 0
    
    with open(nom_fichier, 'w') as fichier:
        fichier.write(str(longueur_dernier_mot))
phrase = "Bonjour tout le monde,moi c'est Malick"
trouver_longueur_dernier_mot(phrase, "longueur.txt")
