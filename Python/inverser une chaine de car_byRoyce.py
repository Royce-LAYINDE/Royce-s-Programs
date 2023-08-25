# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 03:21:10 2023

@author: layin
"""

# Chaîne fournie au départ 
a=str(input("entre le mot: ")) 
  

    #METHODE1
i = len(a) - 1	# le traitement commencera à partir du dernier caractère 
new_a = ""	# nouvelle chaîne à construire (vide au départ) 
while i >= 0: 
 	# on concatène le caractère lu à la nouvelle chaine 
 	new_a+=a[i] 
 	i-=1 
  
# # Affichage du résultat 
# print(a, "=>", new_a)

    #METHODE2
  
# Par découpage de la chaîne (slicing) 
# La séquence est entièrement parcourue en partant de la fin, par pas de -1 
print(a, "=>", a[len(a)::-1])  
  
# Et plus court encore (si le début ou la fin sont omis, ils sont calculés automatiquement) 
print(a, "=>", a[::-1])

    #METHODE3

# reversed renvoie un itérateur de la séquence inversée 
# On joint les éléments de la séquence inversée pour former une chaîne de caractères, 
# en utilisant un séparateur vide 
print(a, "=>", ''.join(reversed(a)))