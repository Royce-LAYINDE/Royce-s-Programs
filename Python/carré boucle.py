import turtle
window= turtle.Screen()
window.title("Dessin d'un carré avec turtle")
t1=turtle.Turtle()
longueur=55
a=0
while a<4:
    t1.fd(longueur)
    t1.left(90)
    a+=1
window.exitonclick()

    
