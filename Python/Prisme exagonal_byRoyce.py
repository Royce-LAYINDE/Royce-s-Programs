import turtle
t1=turtle.Turtle()
longueur= int( input ("Veuillez entrer la dimension de la longueur des cotés de la base: "))
hauteur= int( input ("Veuillez entrer la hauteur du prisme: "))
angle=180*((8-2)/8)
#Début du programme
for i in range(8):
    t1.fd(longueur)
    t1.left(180-angle)
t1.goto(0,-hauteur)

for i in range(8):
    t1.fd(longueur)
    t1.left(180-angle)

t1.fd(longueur)
t1.left(90)
t1.fd(hauteur)
t1.right(45)
t1.fd(longueur)
t1.left(180+45)
t1.fd(hauteur)
t1.right(180-angle)
for i in range(4):
    t1.fd(longueur)
    t1.left(angle-180)
t1.right(angle+180)
t1.fd(hauteur)
t1.right(45)
t1.fd(longueur)
t1.right(-angle+180)
for i in range(2):
    t1.fd(longueur)
    t1.right(90)
    t1.fd(hauteur)
    t1.right(90)
    
