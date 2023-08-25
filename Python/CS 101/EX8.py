# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 23:41:45 2023

@author: lenovo
"""

#COMparaison des caracteres deja triés grace a sorted
def test_anagramme1(chaine1, chaine2):
    return sorted(chaine1) == sorted(chaine2)
mot1 = "listen"
mot2 = "silent"
print(test_anagramme1(mot1, mot2))

#on comptes les occurences de caracteres dans chaque chaine qu'on range dans des dico puis on compare ces derniers
from collections import Counter

def test_anagramme2(chaine1, chaine2):
    compteur1 = Counter(chaine1)
    compteur2 = Counter(chaine2)
    return compteur1 == compteur2
mot1 = "listen"
mot2 = "silent"
print(test_anagramme2(mot1, mot2))

#3e solution
from collections import defaultdict

def test_anagramme3(chaine1, chaine2):
    compteur1 = defaultdict(int)
    compteur2 = defaultdict(int)
    for char in chaine1:
        compteur1[char] += 1
    for char in chaine2:
        compteur2[char] += 1
    return compteur1 == compteur2
mot1 = "listen"
mot2 = "silent"
print(test_anagramme3(mot1, mot2))
