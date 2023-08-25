# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 16:48:53 2023

@author: Royce
"""
#On utilise la propriété d'unicité des élements d'un set
def supprimer_doublons1(tableau):
    elements_uniques = set(tableau)
    return elements_uniques
mytableau = [1, 2, 3, 2, 4, 1, 5, 4, 6]
print(supprimer_doublons1(mytableau))

#On compte le nombre de fois qu'apparait un elt et on decide s'il faut le supprimer ou non
def supprimer_doublons2(tableau):
    nouveau_tableau = []
    for element in tableau:
        if tableau.count(element) > 1:
            if element in nouveau_tableau:                
                continue
            
        nouveau_tableau.append(element)
    return len(nouveau_tableau)
mytableau = [1, 2, 3, 2, 4, 1, 5, 4, 6]
print(supprimer_doublons2(mytableau))

#On utilise une liste sans comptage
def supprimer_doublons3(tableau):
    nouveau_tableau = []
    for element in tableau:
        if element not in nouveau_tableau:
            nouveau_tableau.append(element)
    return len(nouveau_tableau)
mytableau = [1, 2, 3, 2, 4, 1, 5, 4, 6]
print(supprimer_doublons3(mytableau))