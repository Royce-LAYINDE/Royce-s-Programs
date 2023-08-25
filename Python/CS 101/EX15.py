# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 00:32:26 2023

@author: Royce
"""

def rotation_tableau(tableau, k):
    n = len(tableau)
    k = k % n  # Si k dépasse la taille du tableau, ajuste k à sa valeur modulo n

    # Effectue une rotation en trois étapes : inverse, puis inverse les parties gauche et droite
    inverse_tableau(tableau, 0, n - 1)
    inverse_tableau(tableau, 0, k - 1)
    inverse_tableau(tableau, k, n - 1)

def inverse_tableau(tableau, debut, fin):
    while debut < fin:
        tableau[debut], tableau[fin] = tableau[fin], tableau[debut]
        debut += 1
        fin -= 1
tableau = [1, 2, 3, 4, 5]
k = 2
rotation_tableau(tableau, k)
print(tableau)  
