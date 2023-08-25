# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 00:44:54 2023

@author: Royce
"""

def convertir_romain_en_nombre(nombre_romain):
    valeurs_romaines = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    nombre_entier = 0
    i = 0

    while i < len(nombre_romain):
        if i + 1 < len(nombre_romain) and valeurs_romaines[nombre_romain[i]] < valeurs_romaines[nombre_romain[i + 1]]:
            nombre_entier += valeurs_romaines[nombre_romain[i + 1]] - valeurs_romaines[nombre_romain[i]]
            i += 2
        else:
            nombre_entier += valeurs_romaines[nombre_romain[i]]
            i += 1

    return nombre_entier
nombre_romain = "MCMLXXIV"
print(convertir_romain_en_nombre(nombre_romain))  