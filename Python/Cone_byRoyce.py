import turtle as t1
from math import *
import math
#declaration du rayon et de la hauteur
rayon=int(input("entre le rayon de la base de ton cone: "))
hauteur=int(input("entre la hauteur de ton cone: "))
#calcul des longueurs et mesures nécéssaires a la construction
apotheme=sqrt(rayon**2 + hauteur**2)
angle_au_sommet_rad=math.asin(rayon/apotheme)
angle_au_sommet_deg=(angle_au_sommet_rad*180)/pi
#debut constructionn

t1.circle(rayon)
t1.circle(rayon,90)
t1.left(90)

t1.fd(rayon/3)
t1.up()
t1.fd(rayon/3)
t1.down()
t1.fd(rayon/3)


t1.right(90)
t1.fd(hauteur)
t1.right(180-angle_au_sommet_deg)
t1.fd(apotheme)
t1.left(180)
t1.fd(apotheme)
t1.right(angle_au_sommet_deg)
t1.left(180-angle_au_sommet_deg)
t1.fd(apotheme)

