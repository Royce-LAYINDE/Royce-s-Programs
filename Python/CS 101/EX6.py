# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 23:28:42 2023

@author: RoYCE
"""
#operateur de decoupage avec pas négatif
def inversion_chaine1(chaine):
    return chaine[::-1]
chaine = "Bonjour"
print(inversion_chaine1(chaine))

#reversed
def inversion_chaine2(chaine):
    return ''.join(reversed(chaine))
chaine = "Bonjour"
print(inversion_chaine2(chaine))

#concatenation en parttant de l'arriere
def inversion_chaine3(chaine):
    inverse = ''
    for caractere in chaine:
        inverse = caractere + inverse
        print(inverse)
    return inverse
chaine = "Bonjour"
print(inversion_chaine3(chaine))