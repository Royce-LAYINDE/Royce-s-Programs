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
    etudiant = matricule+" : "+nom+" : "+classe+" : "+str(moyenne)+"\n"
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

afficher_fichier()