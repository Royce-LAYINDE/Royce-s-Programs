# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 23:34:08 2023

@author: layin
"""
#Il faut juste changer les extrémités du premier range pour 
for num in range(2, 10):
    if num % 2 == 0:
        print("Nbre pair", num)
        continue
    print("Nbre impair", num)