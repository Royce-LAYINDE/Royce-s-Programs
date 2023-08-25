#Importation de turtle
import turtle

#Initialisation de la fenetre
window= turtle.Screen()

#Donnons un nom à notre fenetre
window.title("Tracé de triangle avec turtle")

#Creation d'une instance de turtle
t= turtle.Turtle()
#--------------------
t.shape("turtle")    # Changer la forme du curseur en "tortue"
t.fillcolor("blue")   #Définir la couleur de remplissage en bleu
t.begin_fill()  #Commencer à remplir la forme
for i in range (4):
    t.fd(50)
    t.lt(90)
t.end_fill()     #Arrêter le remplissage

   


#---------------------
#Ferme la fenetre graphique quand je clique dessus
window.exitonclick()

