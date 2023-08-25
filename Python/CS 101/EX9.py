# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 23:51:19 2023

@author: Royce
"""

def comptage_bits_1(nombre):
    binaire = bin(nombre) 
    compte = 0
    for bit in binaire:
        if bit == '1':
            compte += 1
    return compte
nombre = 137
print(comptage_bits_1(nombre))  # 4
