# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 00:38:11 2023

@author: Royce
"""

def intersection_tableaux_solution1(tableau1, tableau2):
    set1 = set(tableau1)
    set2 = set(tableau2)
    intersection = set1 & set2  # Ou bien: intersection = set1.intersection(set2)
    return list(intersection)
tableau1 = [1, 2, 3, 4, 5]
tableau2 = [4, 5, 6, 7]
print(intersection_tableaux_solution1(tableau1, tableau2))  


#
def intersection_tableaux_solution2(tableau1, tableau2):
    dictionnaire = {}
    intersection = []

    for element in tableau1:
        dictionnaire[element] = True

    for element in tableau2:
        if element in dictionnaire and element not in intersection:
            intersection.append(element)

    return intersection
tableau1 = [1, 2, 3, 4, 5]
tableau2 = [4, 5, 6, 7]

print(intersection_tableaux_solution2(tableau1, tableau2))  
