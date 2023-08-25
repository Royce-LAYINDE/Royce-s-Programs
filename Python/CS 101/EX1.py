# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 15:53:38 2023

@author: Royce
"""

def trouver_indices(tableau, objectif):
    # Parcourir le tableau
    for i in range(len(tableau)):
        for j in range(i+1, len(tableau)):
            # Vérifier si la somme de la paire correspond à l'objectif
            if tableau[i] + tableau[j] == objectif:
                return [i, j]  # Retourner les indices de la paire trouvée
    # Si aucune paire n'est trouvée, retourner None ou un message approprié
    return None

# Exemple d'utilisation
mytableau = [2, 7, 11, 15]
myobjectif = 9
indices = trouver_indices(mytableau, myobjectif)
# if indices:
#     print(f"Les indices des nombres dans la paire sont : {indices[0]}, {indices[1]}")
# else:
#     print("Aucune paire ne donne la somme désirée.")
print(indices)

##OU

def num_cible(nums,cible):

    r = []
    for i,e1 in enumerate(nums):
        for j,e2 in enumerate(nums):
            if e2 + e1 == cible:
                if e1 and e2 not in r:
                    return [i,j]
                    # r.extend([i,j])
    # return r

liste=[1,2,4]
p=num_cible(liste,6)
print(p)