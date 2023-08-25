a=int(input("entrer le nombre de note que vous voulez mettre: "))
liste=[]
for i in range(a):
    x=input("veuillez entrer une note: ")
    liste.append(x)   
    print(liste)
s=0
for i in liste:
    s=s+i
m=s/a

print(m)

    
    

    
