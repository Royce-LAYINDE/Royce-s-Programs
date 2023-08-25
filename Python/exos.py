exercice0
---------
for i in range(10, 15):#permet d'afficher une suite de nombre entre 10 et 14 
    print(i)

for i in range(20,40,2):#affiche les nombres de 20 a 39 avec un pas de 2
    print(i)

for i in range(20):#affiche les nombres divisible par 2
    if i%2 == 0:
       print(i)

for i in range(20):#affiche les nombres non divisibles par 2
    if i%2 != 0:
       print(i)

for i in range(0,1001,2):
    print(i)

for i in range(0,1001,10):
    print(i)

for i in range(0,1001,100):
    print(i)

 for i in range(-15,16):
    print(i)   

for i in range(-30,30,5):
    print(i)

for i in range(50,101,3):
    print(i)

exercice1
---------
N=int(input("saisissez un nombre "))
s=0
for i in range(1,N+1):
    s=s+i
    print(s)

exercice2
---------
import turtle

t1=turtle.Turtle()

longueur=int(input("saisissez la longueur "))
largeur=int(("saisissez la largeur"))

surface=longueur*largeur
perimetre=(longueur+largeur)*2

a=input("voulez vous tracer le rectangle? oui/non")

if a=="oui":
    for i in range(2):
        t1.fd(longueur)
        t1.left(90)
    print("Aurevoir")
if a=="non":
    print("Aurevoir")

exercice3
---------
import turtle

t1= turtle.Turtle()
figure=input("quelle figure voulez vous tracer ")
couleur = input("de quelle couleur doit etre le contour ")

if figure=="cylindre":
    t1.color(couleur)
    t1.circle(60)
    t1.circle(60,90)
    t1.goto(0,100)
    t1.circle(60)
    t1.circle(60,90)
    t1.left(60)
    t1.up()
    t1.fd(100)
    t1.down()
    t1.left(80)
    t1.fd(100)
       
if figure=="pyramide":
    t1.color=couleur
    t1.fd(100)
    t1.left(120)
    t1.fd(100)
    t1.left(120)
    t1.fd(100)
    t1.right(90)
    t1.fd(20)
    t1.right(101)
    t1.fd(103)
    t1.right(100)
    t1.fd(105)
    t1.right(110)
    t1.fd(20)

if figure=="cône":
     t1.color=couleur
     t1.circle(50,450)
     t1.left(30)
     t1.fd(100)
     t1.left(120)
     t1.fd(100)
   
if figure=="prisme hexagonal":
     t1.color=couleur
     t1.color=couleur
     t1.fd(100)
     t1.left(120)
     t1.fd(100)
     t1.left(120)
     t1.fd(100)
     t1.right(90)
     t1.fd(20)
     t1.right(101)
     t1.fd(103)
     t1.right(100)
     t1.fd(105)
     t1.right(110)
     t1.fd(20)

exercice3
---------
t=int(input("saisissez une taille en m"))
m=int(input("saisissez une masse en kg"))
imc=m/t*t
print(imc)
if imc<16,5:
    print("dénutrition")
elif 16,5<imc<18,5:
    print("maigreur")
elif 18,5<imc<25:
    print("masse normale")
elif 25<imc<30:
    print("surpoids")
else:
    print("obésité")

exercice4
---------
import turtle
t1=turtle.Turtle()
t1.color("blue")
t1.pensize(10)
t1.circle(50,180)
t1.goto(0,-10)
t1.left(180)
t1.up()
t1.fd(70)
t1.down()
t1.left(90)
t1.fd(100)
t1.left(180)
t1.up()
t1.fd(100)
t1.down()
t1.right(90)
t1.left(180)
t1.up()
t1.fd(10)
t1.down()
t1.left(60)
t1.fd(120)
t1.right(120)
t1.fd(120)
t1.bk(60)
t1.right(120)
t1.fd(60)
t1.left(60)
t1.up()
t1.fd(60)
t1.left(120)
t1.fd(150)
t1.down()
t1.left(90)
t1.fd(100)
t1.right(90)
t1.fd(50)
t1.right(90)
t1.fd(50)
t1.up()
t1.fd(20)
t1.down()
t1.right(90)
t1.fd(20)
t1.bk(40)
t1.fd(20)
t1.left(90)
t1.fd(30)
t1.right(90)
t1.fd(50)
t1.up()
t1.bk(80)
t1.down()
t1.right(90)
t1.fd(100)
t1.right(160)
t1.fd(110)
t1.left(160)
t1.fd(100)
t1.right(90)
t1.up()
t1.fd(20)
t1.down()
t1.fd(50)
t1.bk(50)
t1.right(90)
t1.fd(50)
t1.left(90)
t1.fd(50)
t1.bk(50)
t1.right(90)
t1.fd(50)
t1.left(90)
t1.fd(50)

exercice5
---------
#declaration des variables
counter = 0
end_value = 100
#permet d'afficher la valeur counter
print("counter value", counter)
#c'est une boucle qui permet d'afficher le counter tant qu'il est<=end_valeur
while counter <= end_value:
    print(counter)
    counter = counter + 1#permet d'augmenter la valeur de 1 a chaque fois
print("counter value", counter)

 #une boucle for est une boucle qui est utilise lorsque le nombre de boucle est connue
#alors boucle while permet de faire quelques choses lorsque une chose est verifier
    
#declaration des variables
counter = 0
end_value = 100
#permet d'afficher la valeur counter
print("counter value", counter)
#c'est une boucle qui permet d'afficher le counter tant qu'il est<=end_valeur
for counter in range(0, end_value+1):
    print(counter)
    counter = counter + 1#permet d'augmenter la valeur de 1 a chaque fois
print("counter value", counter)    

for i in range(10,21,2):
    print(i)

for i in range(20,9,4):
    print(i)

exercice6
---------
#on importe un module nomme turtle
import turtle
tr = turtle.Turtle()
#les variables
pixels = 200
side_count = 0

while side_count < 3:
    if side_count == 0:
        angle = 0
    else:
        angle = 120

    tr.left(angle)
    tr.forward(pixels)
    side_count = side_count + 1

turtle.exitonclick()
