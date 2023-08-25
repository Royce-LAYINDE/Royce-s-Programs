# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 22:55:04 2023

@author: Royce
"""
#On utilise le fait que le carré de la racine carré d'un carré parfait estt égal à ce dernier
import math

def test_carre_parfait1(nombre):
    racine = math.isqrt(nombre)
    return racine * racine == nombre
nombre = 81
print(test_carre_parfait1(nombre))

#On parcourt tous les entiers à partir de 1 jusqu'à la moitié du nombre donné et si le carré de chaque entier est égal au nombre donné, on concus que c'est un carré parfait
def test_carre_parfait2(nombre):
    for i in range(1, nombre // 2 + 1):
        if i * i == nombre:
            return True
    return False
nombre = 81
print(test_carre_parfait2(nombre))
