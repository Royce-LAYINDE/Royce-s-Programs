# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 00:12:12 2023

@author: lenovo
"""
def palindrome1(nombre):
    chaine = str(nombre)
    return chaine == chaine[::-1]
nbr = 12321
print(palindrome1(nbr)) 

#
def palindrome2(nombre):
    if nombre < 10:
        return True
    chaine = str(nombre)
    return chaine[0] == chaine[-1] and palindrome2(int(chaine[1:-1]))
nbr = 12321
print(palindrome2(nbr)) 

#
def palindrome3(nombre):
    nombre_original = nombre
    nombre_inverse = 0

    while nombre > 0:
        reste = nombre % 10
        nombre_inverse = nombre_inverse * 10 + reste
        nombre //= 10

    return nombre_original == nombre_inverse
nbr = 12321
print(palindrome3(nbr)) 