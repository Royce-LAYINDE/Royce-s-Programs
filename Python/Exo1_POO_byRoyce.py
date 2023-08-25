# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 01:32:03 2023

@author: Royce
"""
import turtle
#1-Création d'une classe Rectangle permettant de construire un rectangle dotée d'attributs longueur et largeur


class Rectangle:

    def __init__(self,longueur,largeur):
        self.longueur=longueur
        self.largeur=largeur
        self.t1 = turtle.Turtle()
       
    def Construction(self):
        for i in range(2):
            self.t1.forward(self.longueur)
            self.t1.left(90)
            self.t1.forward(self.largeur)
            self.t1.left(90)
        
#2-Création d'une méthode Perimetre() permettant de calculer le périmètre du rectangle et une méthode Surface() permettant de calculer la surface du rectangle
#3-Créons les getters et setters de suite
    @property
    def Perimetre(self):
        p=2*(self.longueur+self.largeur)
        return p
    
        
    @property
    def Surface(self):
        s=(self.longueur*self.largeur)
        return s
    
#4-Création d'une classe fille Parallelepipede héritant de la classe Rectangle et dotée en plus d’un attribut hauteur et d’une autre méthode Volume() permettant de calculer le volume du Parallélépipède
class Parallelepipede(Rectangle):
    def __init__(self,longueur,largeur,hauteur):
        super().__init__(longueur,largeur)
        self.hauteur=hauteur
    
    @property
    def Volume(self):
        v=(self.longueur*self.largeur*self.hauteur)
        return v   
    

#Vérification 
##Création de deux unstances de classes resp. de Rectangle et de Parall.
mon_rectangle=Rectangle(15, 10) 
mon_parallepipede=Parallelepipede(15, 10, 5)

print(f"le périmètre de mon_rectangle est: {mon_rectangle.Perimetre}") 
print(f"L'aire de mon_rectangle est: {mon_rectangle.Surface}")
print(f"Le volume de mon_parallepipede est: {mon_parallepipede.Volume}")
