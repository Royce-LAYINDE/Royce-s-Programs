# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 00:41:36 2023

@author: Royce
"""

def nombre_chemins_uniques(grille):
    m = len(grille)
    n = len(grille[0])

    # Création d'une grille aux mêmes dimensions pour stocker le nombre de chemins uniques
    chemins = [[0] * n for _ in range(m)]

    # Nombre de chemins uniques pour atteindre le coin supérieur gauche est 1
    chemins[0][0] = 1

    # Calcul des nombres de chemins uniques pour chaque case de la grille
    for i in range(m):
        for j in range(n):
            if i > 0:
                chemins[i][j] += chemins[i-1][j]  # Ajout des chemins venant du haut
            if j > 0:
                chemins[i][j] += chemins[i][j-1]  # Ajout des chemins venant de la gauche

    return chemins[m-1][n-1]  # Nombre de chemins uniques pour atteindre le coin inférieur droit
grille = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
print(nombre_chemins_uniques(grille))  # 6
