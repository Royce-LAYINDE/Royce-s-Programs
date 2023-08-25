e=0
A=int(input("Combien de notes veut tu saisir?"))
Note=list(input("Entre les notes: "))
while len(Note)==A:
    
    for i in Note:
        e=e+i
print("La somme des notes est:", e)
M=e/len(Note)
print("La moyenne est:",M)


