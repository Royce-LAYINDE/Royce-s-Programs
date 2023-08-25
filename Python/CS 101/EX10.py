# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 23:54:47 2023

@author: Royce
"""

def fusion_2tableaux_tries(tableau1, tableau2):
    fusion = []
    i = 0  
    j = 0  

   
    while i < len(tableau1) and j < len(tableau2):
        if tableau1[i] <= tableau2[j]:
            fusion.append(tableau1[i])
            i += 1
        else:
            fusion.append(tableau2[j])
            j += 1

 
    while i < len(tableau1):
        fusion.append(tableau1[i])
        i += 1

   
    while j < len(tableau2):
        fusion.append(tableau2[j])
        j += 1

    return fusion
tableau1 = [1, 3, 5, 7, 9]
tableau2 = [2, 4, 6, 8, 10]
resultat_fusion = fusion_2tableaux_tries(tableau1, tableau2)
print(resultat_fusion)

#
import heapq

def fusion_2tableaux_tries(tableau1, tableau2):
    return list(heapq.merge(tableau1, tableau2))
tableau1 = [1, 3, 5, 7, 9]
tableau2 = [2, 4, 6, 8, 10]
resultat_fusion = fusion_2tableaux_tries(tableau1, tableau2)
print(resultat_fusion)

