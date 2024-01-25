# Fonction de saisie des informations d'un employé
def saisir_info_employe():
    matricule = input("Matricule de solde: ")
    nom = input("Nom: ")
    prenom = input("Prénom: ")
    fonction = input("Fonction: ")
    titre = input("Titre: ")
    service = input("Service: ")
    date_embauche = input("Date d'embauche (format JJ/MM/AAAA): ")
    salaire_base = float(input("Salaire de base: "))
    situation_matrimoniale = input("Situation matrimoniale: ")
    
    return f"{matricule},{nom},{prenom},{fonction},{titre},{service},{date_embauche},{salaire_base},{situation_matrimoniale}\n"

# Fonction qui crée le fichier d'employés
def creer_fichier_employes():
    f = open("liste_employé.txt","w")
    rep= "y"
    while rep.lower()=="y":
        employes = saisir_info_employe()
        f.write(employes)
        print("Employé enrégistré avec succes")
        print("Voulez vous ajouter un autre employé?(y/n) : ", end = "")
        rep = input("")
    f.close()
creer_fichier_employes()

# Fonction qui affiche la liste des employés
def afficher_liste_employes(employes):
    for employe in employes:
        print(employe)

# Fonction qui transfère le contenu du fichier dans deux listes
def transfert_sexe(employes):
    hommes = [employe for employe in employes if employe.split(',')[4].lower() == "homme"]
    femmes = [employe for employe in employes if employe.split(',')[4].lower() == "femme"]
    return hommes, femmes

# Fonction qui affiche le contenu d'une liste
def afficher_contenu_liste(liste):
    for element in liste:
        print(element)

# Fonction qui détermine et affiche le nombre d'ingénieurs et d'employés dans le service "administration"
def stats_titre_service(employes):
    ing_count = len([employe for employe in employes if employe.split(',')[4].lower() == "ingénieur"])
    admin_count = len([employe for employe in employes if employe.split(',')[5].lower() == "administration"])
    
    print(f"Nombre d'ingénieurs: {ing_count}")
    print(f"Nombre d'employés dans le service 'administration': {admin_count}")

# Fonction pour le menu
def menu():
    employes = []

    # Saisir une dizaine d'employés
    # for _ in range(10):
    #     employes.append(saisir_info_employe())

    # # Créer le fichier d'employés
    # creer_fichier_employes(employes)

    # Lire le fichier d'employés
    with open("employes.txt", "r") as fichier:
        lignes = fichier.readlines()

    # Afficher la liste des employés
    afficher_liste_employes(lignes)

    # Transférer le contenu du fichier dans deux listes
    hommes, femmes = transfert_sexe(lignes)
    print("\nHommes:")
    afficher_contenu_liste(hommes)
    print("\nFemmes:")
    afficher_contenu_liste(femmes)

    # Afficher le nombre d'ingénieurs et d'employés dans le service "administration"
    stats_titre_service(lignes)

# Appeler le menu
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
            reer_fichier_employes()
        elif choix == 2:
            afficher_liste_employes()
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
