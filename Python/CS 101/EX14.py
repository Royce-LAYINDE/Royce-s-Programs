# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 00:28:57 2023

@author: Royce
"""

def sous_chaine_somme_maximale(tableau):
    if not tableau:
        return None
    
    somme_max = float('-inf')
    somme_actuelle = 0
    debut = 0
    debut_max = 0
    fin_max = 0
    
    for i in range(len(tableau)):
        somme_actuelle += tableau[i]
        
        if somme_actuelle > somme_max:
            somme_max = somme_actuelle
            debut_max = debut
            fin_max = i
        
        if somme_actuelle < 0:
            somme_actuelle = 0
            debut = i + 1
    
    return tableau[debut_max:fin_max+1]
tableau = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
resultat = sous_chaine_somme_maximale(tableau)
print(resultat)  # [4, -1, 2, 1]


