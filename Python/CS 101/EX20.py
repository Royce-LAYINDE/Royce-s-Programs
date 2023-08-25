# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 00:43:03 2023

@author: Royce
"""

def plus_long_prefixe_commun(ensemble_chaines):
    if not ensemble_chaines:
        return ""

    prefixe = ""
    premiere_chaine = ensemble_chaines[0]
    longueur_minimale = min(len(chaine) for chaine in ensemble_chaines)

    for i in range(longueur_minimale):
        caractere_courant = premiere_chaine[i]
        if all(chaine[i] == caractere_courant for chaine in ensemble_chaines):
            prefixe += caractere_courant
        else:
            break

    return prefixe
ensemble_chaines = ["abcd", "abcde", "abc", "ab"]
print(plus_long_prefixe_commun(ensemble_chaines))  # "ab"
