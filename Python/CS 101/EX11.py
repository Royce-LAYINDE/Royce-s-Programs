# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 00:02:33 2023

@author: Royce
"""

def triangle_de_pascal(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        triangle = triangle_de_pascal(n - 1)
        ligne_precedente = triangle[-1]
        nouvelle_ligne = [1]
        for i in range(len(ligne_precedente) - 1):
            somme = ligne_precedente[i] + ligne_precedente[i + 1]
            nouvelle_ligne.append(somme)
        nouvelle_ligne.append(1)
        triangle.append(nouvelle_ligne)
        return triangle
n = 5
resultat = triangle_de_pascal(n)
for ligne in resultat:
    print(ligne)
