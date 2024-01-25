# Fonction de saisie des informations d'un employé
def saisir_info_employe():
    print(" - "*25)
    print("Saisie des informations de l'employé: ")
    print(" - "*25)
    matricule_solde = input("Veuillez saisir le matricule de solde: ")
    nom = input("Veuillez saisir le nom de l'employé: ")
    prenom = input("Veuillez saisir le prénom de l'employé: ")
    titre = input("Veuillez saisir le titre de l'employé: ")
    fonction = input("Veuillez saisir la fonction de l'employé: ")
    service = input("Veuillez saisir le service de l'employé: ")
    sexe = input("Veuillez saisir le sexe de l'employé M/F: ")
    date_embauche = input("Veuillez saisir la Date d'embauche (format JJ/MM/AAAA): ")
    situation_matrimoniale = input("Veuillez saisir la situation matrimoniale de l'employé: ")
    salaire_base = input("Veuillez saisir le salaire de base de l'employé: ")
    employe = matricule_solde + " : " + nom + " : " + prenom + " : " + titre + " : " + fonction + " : " + service + " : " + sexe + " : " + date_embauche + " : " + situation_matrimoniale + " : " + salaire_base + "\n"
    return employe

# Fonction qui crée le fichier d'employés
def creer_fichier_employes():
    f = open("liste_employe.txt","w")
    rep= "y"
    while rep.lower()=="y":
        employes = saisir_info_employe()
        f.write(employes)
        print("Employé enrégistré avec succes")
        print("Voulez vous ajouter un autre employé?(y/n) : ", end = "")
        rep = input("")
    f.close()

def ajouter_fichier_employes():
    f = open("liste_employe.txt","a")
    rep= "y"
    while rep.lower()=="y":
        employes = saisir_info_employe()
        f.write(employes)
        print("Employé enrégistré avec succes")
        print("Voulez vous ajouter un autre employé?(y/n) : ", end = "")
        rep = input("")
    f.close()

# Fonction qui affiche la liste des employés
def afficher_fichier_employes():
    f = open("liste_employe.txt","r")
    employes = f.readlines()
    affiche_liste(employes)
    f.close()

#Fonction qui transfere le contenu dans une liste

def transfert(sexe_p):
    f = open("liste_employe.txt","r")
    employes = f.readlines()
    liste= []
    for employe in employes:
        sexe = employe.split(" : ")[6]
        if sexe.upper() == sexe_p:
            liste.append(employe)
    f.close()
    return liste

#une fct qui recoit une liste et affiche son contenu

def affiche_liste(employes):
    if len(employes)==0:
        print("La liste est vide.")
    else: 
        for employe in employes:
            e = employe.split(" : ")
            for i in e:
                print(i, end=" ")
            print("")   


# une fct qui determine et affiche le nbre d'employés dont le titre est "ingénieur" et 
# le nbre d'employé qui travaille dans le service "administration"

def nombre_employes():
    f = open("liste_employe.txt","r")
    employes = f.readlines()
    compteur1 = 0
    compteur2 = 0 
    if len(employes)==0:
        print("La liste est vide")
    else:
        for employe in employes:
            titre = employe.split(" : ")[3]
            service = employe.split(" : ")[5]
            if titre.lower() =="ingénieur":
                compteur1 +=1
            if service.lower() =="administration":
                compteur2 +=1
        
        print("Le nombre d'employé de titre ingénieur est ",compteur1)
        print("Le nombre d'employé du service administration est ",compteur2)

#une fct qui determine et affiche 
# les employés dont le salaire depasse la moyenne salariale des employés ainsi que leur effectif

def gros_salaires():
    f = open("liste_employe.txt","r")
    employes = f.readlines()
    sum_salaires = 0
    if len(employes)==0:
        print("La liste est vide")
    else:
        for employe in employes:
            salaire= float(employe.split(" : ")[9])
            sum_salaires+= salaire
        moy_salaire = sum_salaires/ len(employes)
        effectif = 0
        for employe in employes:
            salaire= float(employe.split(" : ")[9])
            if salaire > moy_salaire:
                e = employe.split(" : ")
                effectif += 1
                for i in e:
                    print(i, end=" ")
                print("") 
        print("Le nombre d'employé dont le salaire depasse la moyenne salariale est",effectif) 

#MENU
def menu():

    while True:
        print("Bienvenue sur le menu")
        print("Taper 1 pour créer un fichier contenant les infos des employés ")
        print("Taper 2 pour afficher la liste des employés déjà contenu dans votre fichier ")
        print("Taper 3 pour afficher la liste des employés classés par sexe")
        print("Taper 4 pour afficher le nombre d'employés dont le titre est ingénieur et le nombre d'employés dont le service est adiministration ")
        print("Taper 5 pour ajouter de nouveaux employés au fichier ")
        print("Taper 6 pour afficher les employés avec des salaires supérieurs à la moyenne salariale ")
        print("Taper 7 pour Quitter le Menu ")
        print("Faites votre choix: ", end=" ")
        choix= int(input())

        if choix == 1:
            creer_fichier_employes()
        if choix == 2:
            afficher_fichier_employes()
        if choix == 3:
            liste_masculin= transfert("M")
            liste_feminin= transfert("F")  
            print("Voici la liste des employes masculin: ")
            affiche_liste(liste_masculin)
            print("Voici la liste des employes feminin: ")   
            affiche_liste(liste_feminin) 
        if choix == 4:
            nombre_employes()      
        if choix == 5:
            ajouter_fichier_employes()
        if choix == 6:
            gros_salaires()
        if choix == 7:
            print("Au plaisir de vous revoir!!")
            break
        else:
            print("Erreur de choix, veuillez entrer un choix correct")

menu()