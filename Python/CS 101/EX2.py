# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 16:14:38 2023

@author: Royce
"""
#On compare les caractères de la chaîne de chaque extrémité vers le centre, en vérifiant si les caractères correspondants sont identiques.
def test_palindrome1(chaine):
    chaine = chaine.lower()  # Convertir la chaîne en minuscules pour ignorer la casse
    i = 0
    j = len(chaine) - 1
    while i < j:
        if chaine[i] != chaine[j]:
            return False
        i += 1
        j -= 1
    return True
chaine = "radar"
print(test_palindrome1(chaine))

#On inverse la chaîne et vérifie si la version inversée est identique à la version originale.
def test_palindrome2(chaine):
    chaine = chaine.lower()  # Convertir la chaîne en minuscules pour ignorer la casse
    chaine_inverse = chaine[::-1]
    return chaine == chaine_inverse
chaine = "radar"
print(test_palindrome2(chaine))

#On utilise une approche récursive pour vérifier si la chaîne est un palindrome en comparant les caractères aux extrémités. On divise ainsi le problème en sous-problèmes plus petits.
def test_palindrome3(chaine):
    chaine = chaine.lower()  # Convertir la chaîne en minuscules pour ignorer la casse
    if len(chaine) <= 1:
        return True
    elif chaine[0] != chaine[-1]:
        return False
    return test_palindrome3(chaine[1:-1])
chaine = "paoup"
print(test_palindrome3(chaine))

#On utilise reversed et on l'associe avec join pour pouvoir concatener les caracteres qui en sortent
def test_palindrome4(chaine):
    chaine = chaine.lower()  # Convertir la chaîne en minuscules pour ignorer la casse
    chaine_inverse = ''.join(reversed(chaine))
    return chaine == chaine_inverse
chaine = "radar"
print(test_palindrome4(chaine))