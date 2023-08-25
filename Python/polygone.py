import turtle
t1=turtle.Turtle()
a=int(input("Entre le nombre de cotés de ton polygone: "))
longueur= int( input ("Veuillez entrer la dimension de la longueur des cotés"))
couleur= input ("Veuillez entrer une couleur")
angle=180-(180*((a-2)/a))
#Début du programme
t1.color(couleur)
for i in range(a):
    t1.fd(longueur)
    t1.left(angle)
