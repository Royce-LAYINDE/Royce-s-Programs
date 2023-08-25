# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 00:34:33 2023

@author: Royce
"""

def trouver_nombre_manquant_solution1(tableau):
    n = len(tableau) + 1  # Nombre total d'éléments attendus, y compris le nombre manquant
    somme_attendue = (n * (n + 1)) // 2  # Somme totale attendue des nombres de 1 à n
    somme_reelle = sum(tableau)  # Somme réelle des nombres présents dans le tableau
    nombre_manquant = somme_attendue - somme_reelle
    return nombre_manquant
tableau = [1, 2, 4, 5]  
print(trouver_nombre_manquant_solution1(tableau))  



#
def trouver_nombre_manquant_solution2(tableau):
    n = len(tableau) + 1  # Nombre total d'éléments attendus, y compris le nombre manquant
    ensemble_nombres = set(tableau)  # Ensemble des nombres présents dans le tableau
    
    for nombre in range(1, n + 1):
        if nombre not in ensemble_nombres:
            return nombre
tableau = [1, 2, 4, 5]  

print(trouver_nombre_manquant_solution2(tableau))  
