# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import turtle
import math
t1=turtle.Turtle()
a="carré"
b="triangle"
c="rectangle"
d="équilatéral"
e="isocèle"
n=input("saisi le nom d'une figure que tu veux entre carré, rectangle et triangle: ")
color= input ("Veuillez entrer une couleur pour votre figure: ")
if n==a:
    longueur= int( input ("Veuillez entrer la dimension de votre longueur"))
    
    t1.color(color)
    for i in range(4):
        t1.fd(longueur)
        t1.left(90)

if n==b:
    m=input("Quelle est sa nature?(rectangle,isocèle,équilatéral)  ")
    if m==c:
        base = int(input("Entrez la longueur de la base du triangle : "))
        hauteur = int(input("Entrez la hauteur du triangle : "))    
        angle =math.degrees(math.atan(base/hauteur)) 
        angletwo =math.degrees(math.atan(hauteur/base)) 
        turtle.left(90)
        turtle.forward(hauteur)
        turtle.left(180-angle)
        turtle.forward((base**2 + hauteur**2)**0.5)
        turtle.left(180-angletwo)
        turtle.forward(base)
   # if m==e:
    
    if m==d:
        longueur= int( input ("Veuillez entrer la dimension des cotés de votre triangle équilatéral"))
        t1.color(color)
        for i in range(3):
            t1.fd(longueur)
            t1.left(120)
if n==c:
    longueur= int( input ("Veuillez entrer la dimension de votre longueur"))
    largeur= int(input ("Veuillez entrer la dimension de votre largeur"))
    for i in range(2):
        t1.color(color)
        t1.fd(longueur)
        t1.left(90)
        t1.fd(largeur)
        t1.left(90)
        
                         


