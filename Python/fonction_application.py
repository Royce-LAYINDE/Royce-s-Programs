#import de la bibliotheque turtle
import turtle
t1=turtle.Turtle()
#definition de notre fonction application
def application():
    r=int(input("Veuillez taper 1 pour tracer un carre, 2 pour un rectangle, 3 pour un triangle rectangle: "))
    if r==1:
        print("Vous allez tracer un carre")
        def carre(longueur,couleur):
            t1.color("blue")
            for i in range(4):
                t1.fd(100)
                t1.left(90)
            t1.penup ()
            t1.right (90)
        carre(100,"blue")
    elif r==2:
         print("Vous allez tracer un rectangle")
         def rectangle(longueur,largeur,couleur):
             t1.forward (50)
             t1.pendown()
             t1.color("green")
             for i in range(2):
                 t1.fd(200)
                 t1.left(90)
                 t1.fd(100)
                 t1.left(90)
             t1.penup ()
             t1.right (90)
         rectangle(200,100,"green")
    else:
        print("Vous allez tracer un triangle rectangle")
        def triangle_rectangle(l1,l2,l3,couleur):
            t1.forward (50)
            t1.pendown() 
            t1.color("red")
            t1.fd(150)
            t1.left(90)
            t1.fd(90)
            t1.left(120)
            t1.fd(174.92)
        triangle_rectangle(150,90,174.92,"red")
application()       
        
         
        
        
        
        
