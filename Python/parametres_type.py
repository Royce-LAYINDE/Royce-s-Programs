#Dans la fonction suivante les parametres sont positionnels ou obligatoires
def additionner(a,b,c):
    s = a+b+c
    return s

#Dans la fonction suivante a est obligatoire b et c optionnels
def additionner2(a,b=5,c=10):
    s = a + b + c
    return s
#Les parametres optionnels arrivent tjrs apres ceux positionnels
#return: mot cle permettant de renvoyer une valeur
#NB: print != return

def additionner3(a,b=5,c=10):
    s = a + b + c
    print (s)

r2=additionner2(7)
r3=additionner3(7)

print(r2)
print(r3)

#On dit que additionner3 est une procedure car elle ne renvoie rien du tout
#On dit que additionner2 est une fonction car elle renvoie une information
#Le mot cle return peut apparaitre +sieurs fois dans la fonction

def cafe(choix):
    if choix == 1:
        return "Cafe noir"
    elif choix == 2:
        return "Cafe avec sucre"
    else:
        return "Cafe avec du lait"
#Apres le mot cle return plus rien ne s'execute
