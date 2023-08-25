# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 23:08:34 2023

@author: Royce
"""
#on utilise un dictionnaire pour stocker les éléments du tableau en tant que clés et leur nombre d'occurrences en tant que valeurs.
def comptage_occurrences1(tableau):
    compteur = {}
    for element in tableau:
        compteur[element] = compteur.get(element, 0) + 1
    return compteur
tableau = [1, 2, 3, 2, 4, 1, 5, 4, 6]
print(comptage_occurrences1(tableau)) 

#On utilise la classe Counter du module collections de Python
from collections import Counter

def comptage_occurrences2(tableau):
    compteur = Counter(tableau)
    return compteur

tableau = [1, 2, 3, 2, 4, 1, 5, 4, 6]
print(comptage_occurrences2(tableau))

#on utilise un dictionnaire pour stocker les éléments du tableau en tant que clés et leur nombre d'occurrences en tant que valeurs.
def comptage_occurrences3(tableau):
    compteur = {}
    for element in tableau:
        if element in compteur:
            compteur[element] += 1
        else:
            compteur[element] = 1
    return compteur
tableau = [1, 2, 3, 2, 4, 1, 5, 4, 6]
print(comptage_occurrences3(tableau))