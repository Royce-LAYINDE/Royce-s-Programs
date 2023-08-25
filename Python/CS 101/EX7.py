# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 23:38:03 2023

@author: Royce
"""

def sommation_digits(nombre, nom_fichier):
    somme = 0
    for i in range(1, nombre + 1):
        somme += i
    
    with open(nom_fichier, 'w') as fichier:
        fichier.write(str(somme))
sommation_digits(3, "sommedigits.txt")
