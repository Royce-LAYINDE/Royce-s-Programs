#import de la bibliotheque Turtle et création du curseur
import turtle
t1=turtle.Turtle()

#Création de nos variables
longueur= int( input ("Veuillez entrer la dimension de votre longueur"))
color= input ("Veuillez entrer une couleur")
angle= int (input ("Veuillez entrer la mesure des angles de votre triangle équilatéral"))
#Début du programme
t1.color(color)
t1.fd(longueur)
t1.left(angle)
t1.fd(longueur)
t1.left(angle)
t1.fd(longueur)

