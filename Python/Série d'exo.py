#0
#-executer puis analyser
for i in range(10,15):
    print(i)
#cette boucle renvoit tous les nombres compris dans l'intervalle [10,15[
print("bye")
for i in range(20,40,2):
    print(i)
#celle ci renvoie la suite de nbres de [20,40[ mais par bond de 2
print("bye")
for i in range(20):
    if i%2==0:
        print(i)
#renvoie les nbrs <20 s'ils sont pairs
print("bye")
for i in range(20):
    if i%2 !=0:
        print(i)
#renvoie les nbrs <20 s'ils sont impairs
print("bye")
#-Ecriture
#-qui affiche les nombres de 0 à 1000 de 2 en 2
for i in range(0,1000,2):
    print(i)

  #- qui affiche les nombres de 0 à 1000 de 10 en 10
for i in range(0,1000,10):
    print(i)

  #- qui affiche les nombres de 0 à 1000 de 100 en 100
for i in range(0,1000,100):
    print(i)

  #- qui affiche les nombres de -15 à 15
for i in range(-15,15):
    print(i)

  #- qui affiche les nombres de -30 à 30 de 5 en 5
for i in range(-30,30,5):
    print(i)

  #- qui affiche les nombres de 50 à 100 de 3 en 3
for i in range(50,100,3):
    print(i)
#ex1
N=int(input("Entrer un nbre: "))
a=0
for i in range(N+1):
   a=i+a
print(a)
#ex2
long=int(input("longueur? "))
lar=int(input("largeur? "))
s=long*lar
p=(long+lar)*2
print("la surface est: ", s)
print("le périmetre est: ", p)

rep=input("Veux-tu tracer le rectangle? ")
if rep=="oui":
    import turtle
    t1=turtle.Turtle()
    for i in range(2):
        t1.fd(long)
        t1.left(90)
        t1.fd(lar)
        t1.left(90)
        print("Au-revoir")
elif rep=="non":
    print("au-revoir")
else:
    print("mauvaise entrée")
#ex2-1
import turtle

#cylindre
polygon = turtle.Turtle()
polygon.circle(50)
polygon.fd(150)
polygon.circle(50)
polygon.circle(50,180)
polygon.left(180)
polygon.left(180)
polygon.fd(150)

turtle.exitonclick()

    




