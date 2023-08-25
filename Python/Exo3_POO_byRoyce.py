# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 14:15:33 2023

@author: Royce
"""
from math import sqrt
from math import pi


#1- Dénissons une classe Cercle permettant de créer un cercle C(O,r) de centre O(a,b) et de rayon r à l'aide duconstructeur

class Cercle:
    
    def __init__(self,a,b,r):
        self.a = a 
        self.b = b
        self.r = r
        
#2-Dénissons une méthode Surface() de la classe qui permet de calculer la surface du cercle
    
    def surface(self):       
        return pi*(self.r**2)
    
#3- Dénissons une méthode Perimetre() de la classe qui permet de calculer le périmètre du cercle

    def perimetre(self):
        return 2*pi*self.r
    
#4- Dénissons une méthode testAppartenance() de la classe qui permet de tester si un point A(x,y) appartient ou non au cercle C(O,r)
    
    def test_appartenance(self,x,y):
        distance = sqrt(((self.a + self.b) ** 2) + ((x + y) ** 2))
        return distance == self.r #(1)
 #(1)<=># if distance == self.r:
        #     #(f"Le point de coordonnées ({x},{y}) appartient au cercle C(O,r) ")
        #     return True
        # else:
        #     #(f"Le point de coordonnées ({x},{y}) n'appartient pas au cercle C(O,r) ")
        #     return False
        
print(type(Cercle))       
#Verification
mon_cercle=Cercle(5,7,10)
print(mon_cercle.surface())
print(mon_cercle.perimetre())
print(mon_cercle.test_appartenance(2, 3))