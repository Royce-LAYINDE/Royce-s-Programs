#1
print ("EXo:Racine d'un nbre")
from math import*
n=float(input("entre le nbre"))
if n>=0:
    r= sqrt(n)
    print("la racine de", n, "est", round(r,3))
    
else:
    print("Impossible d'éffectuer la racine d'un nombre négatif")
print("Au_revoir")
#2
print ("EXo:Comparaison de deux mots")
n1=str(input("entre un mot"))
n2=str(input("entre un second mot"))
if n1<n2:
    print("le mot le plus petit est", n1)
else:
    print("le mot le plus petit est", n2)

print("Au_revoir")
#ou
print ("EXo:2e méthode(code plus compact)")
print("entre deux mots")
n1=str(input())
n2=str(input())
a=n1 if n1<n2 else n2
print("le mot le plus petit est", a)
print("Au_revoir")
#3
print("exo:SEcurisation d'une enceinte pressurisée")
pseuil=2.3
vseuil=7.41
pression=float(input("entre la pression courante de l'enceinte"))
volume=float(input("entre le volume courant de l'enceinte"))
if (pression>pseuil) and (volume>vseuil):
    print("arret immédiat de l'enceinte")
elif (pression>pseuil) and (volume<vseuil):
     print("augmenter le volume de l'enceinte")
elif pression<pseuil and volume>vseuil:
     print("diminuer le volume de l'enceinte")
else:
            print("tout va bien")
print("au revoir")
#4

a,b=0,10
while a<b:
    print(a, end=" ")
    a = a + 1

print("aurevoir")
b=10
while b!=0:
    b=b-1
    if b%2!=0:
        print(b, end=" ")
print("aurevoir")
        
#5

n=int(input("entre un nombre appartenant à[1..10]: "))
while not(1<= n<=10):
    n= int(input("tu as entré un nbre qui n'est pas dans l'intervalle, réessaye: "))
print("tu as entré", n)

#6
n=str(input("ecrit une chaine(mot ou prhase): "))
print("ta chaine est composée de:")
for lettre in n:
    print(lettre)
b=[]
n=int(input("Combien de mots veux tu saisir?"))
for i in range(n):
    a=input(f"veuillez saisir le nombre {i+1}")
    b.append(a)
    print (b)
for i in b:
    print(i,end=" ")
#7
    for i in range(0,15,3):
        print (i)
#8
for i in range(1,11):
    if i==5:
        break
    else:
        print(i)
#9
for i in range(1,11):
    if i==5:
        continue
    else:
        print(i)
