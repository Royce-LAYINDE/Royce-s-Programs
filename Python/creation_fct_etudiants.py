# ecrire un script python contenant les fonctions suivantes
# -une fct de saisie des informations d'un etudiant
# -une fct de creation d'un fichier d'un etudiant
# -une fct qui affiche le contenu du fichier de l'etudiant
# -une fct qui permet d'ajouter des etudiants dans le fichier
# -une fct qui transfert dans une liste le contenu du fichier de l'etudiant
# -une fct qui affiche la liste des etudiants avec la moyenne la plus grande et la moyenne la plus petite
# -une fct pour le menu
# Etudiant(Matricule, Nom, Prenom, Classe, Moyenne)

def saisie_etudiant():
    print(" - " * 25)
    print("Saisie des informations d'un étudiant...")
    print(" - " * 25)
    matricule = input("Saisir le matricule de l'étudiant: ")
    nom = input("Veuillez entrer le nom de l'étudiant: ")
    prenom = input("Veuillez entrer le prenom de l'etudiant: ")
    classe = input("Veuillez entrer la classe de l'étudiant: ")
    moyenne = float(input("Veuillez entrer la moyenne de l'étudiant: "))
    print(" - " * 25)
    etudiant = matricule+" : "+nom+" : "+prenom+" : "+classe+" : "+str(moyenne)+"\n"
    return etudiant

def creation_fichier():
    f = open("liste_etudiant.txt","w")
    rep= "y"
    while rep.lower()=="y":
        etudiant = saisie_etudiant()
        f.write(etudiant)
        print("Etudiant enrégistré avec succes")
        print("Voulez vous ajouter un autre étudiant?(y/n) : ", end = "")
        rep = input("")
    f.close()

#Appel de la fonction creation 
creation_fichier()

def afficher_fichier():
    f = open("liste_etudiant.txt", "r")
    etudiants = f.readlines() #la variable sera une liste
    print(" - " * 25)
    print("Voici le contenu de votre fichier")
    print(" - " * 25)
    for etu in etudiants:
        e= etu.split(" : ")
        for i in e:
            print(i, end=" ")
    f.close()



# afficher_fichier()

def ajout_etudiants_fichier():
    f = open("liste_etudiant.txt","a")
    rep= "y"
    while rep.lower()=="y":
        etudiant = saisie_etudiant()
        f.write(etudiant)
        print("Etudiant enrégistré avec succes")
        print("Voulez vous ajouter un autre étudiant?(y/n) : ", end = "")
        rep = input("")
    f.close()
# ajout_etudiants_fichier()
# afficher_fichier()

#
def transfert_etudiant_fichier_vers_liste():
    f = open("liste_etudiant.txt", "r")
    etudiants = f.readlines() #la variable sera une liste
    f.close()
    return etudiants

# new_liste = transfert_etudiant_fichier_vers_liste() #on appelle la fct sur la liste initialisée et on lui affecte cette valeur nouvelle obtenue

#
def traitement_liste(etudiants):
    if len(etudiants)== 0:
        print("La liste est vide")
    else:
        max_etudiant= etudiants[0]
        min_etudiant= etudiants[0]
        max_moyenne= float(etudiants[0].split(" : ")[4])
        min_moyenne= float(etudiants[0].split(" : ")[4])
        for etu in etudiants:
            e= etu.split(" : ")
            moyenne  = float(e[4])
            if moyenne > max_moyenne:
                max_moyenne = moyenne 
                max_etudiant = etu 
            elif moyenne < min_moyenne:
                min_moyenne = moyenne
                min_etudiant = etu
            for i in e:
                print(i, end=" ")
        print(" - " *20)
        print("L'etudiant qui a la plus grande moyenne est: ")
        print(max_etudiant)
        print("L'etudiant qui a la plus petite moyenne est: ")
        print(min_etudiant)

# traitement_liste(new_liste)

#menu
def menu():
    
    while True:
            
        print("Bienvenu sur le menu. Voici les choix qu s'offrent à vous: ")
        print("Taper 1 pour créer un fichier contenant les informations relatives à des étudiants.")
        print("Taper 2 pour afficher le contenu de votre fichier sur les étudiants.")
        print("Taper 3 pour ajouter un nouvel étudiant à votre fichier.")
        print("Taper 4 pour afficher l'étudiant avec la plus grande moyenne et l'étudiant avec la plus petite moyenne.")
        print("Taper 5 pour quitter.")
        choix= int(input("Quel est votre choix ?  "))
        
        if choix == 1:
            creation_fichier()
        elif choix == 2:
            afficher_fichier()
        elif choix == 3:
            ajout_etudiants_fichier
        elif choix == 4:
            liste = transfert_etudiant_fichier_vers_liste()
            traitement_liste(liste)

        elif choix == 5:
            print("Merci et au revoir")
            break
        else:
            print("Veuillez entrer une option valide")
menu()