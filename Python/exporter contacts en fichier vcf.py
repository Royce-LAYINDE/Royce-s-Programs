# -*- coding: utf-8 -*-
"""
author: M.Royce
"""
#Cration d'une liste contenant les informations de chaque personne (nom, numéro de téléphone)
contacts = [
    ("Jean Dupont G2", "77 123 45 67"),
    ("Marie Martin G2", "77 234 56 78"),
    ("Pauline Dubois G2", "78 345 67 89"),
    ("Alex Tremblay G2", "77 987 65 43"),
    ("Sophie Lavoie G2", "78 876 54 32"),
    ("Pierre Leblanc G2", "77 654 32 10"),
    ("Isabelle Gagnon G2", "77 890 12 34"),
    ("François Roy G2", "78 567 89 01"),
    ("Émilie Côté G2", "77 123 45 67"),
    ("Vincent Boucher G2", "78 234 56 78"),
    ("Catherine Martel G2", "77 345 67 89"),
    ("David Fortin G2", "78 987 65 43"),
    ("Julie Beaulieu G2", "77 876 54 32"),
    ("Nicolas Girard G2", "77 654 32 10"),
    ("Valérie Caron G2", "78 890 12 34"),
    ("Martin Bergeron G2", "77 567 89 01"),
    ("Mélanie Renaud G2", "78 123 45 67"),
    ("Mathieu Lévesque G2", "77 234 56 78"),
    ("Audrey Deschênes G2", "77 345 67 89"),
    ("Sébastien Rousseau G2", "78 987 65 43"),
    ("Lucie Fournier G2", "77 876 54 32"),
    ("Maxime Gauthier G2", "77 654 32 10"),
    ("Caroline Dufresne G2", "78 890 12 34"),
    ("Richard Beaudoin G2", "77 567 89 01"),
    ("Ariane Giroux G2", "78 123 45 67"),
    ("Philippe Bélanger G2", "77 234 56 78")
]

# Initialisation de la variable qui contiendra toutes les vCards
listes_de_tous_les_contacts = ""

# Parcours de chaque contact dans la liste
for contact in contacts:
    nom = contact[0]
    numero = contact[1]

    # Création du contenu d'une vCard pour le contact actuel
    contenu_d_un_contact = f"BEGIN:VCARD\nVERSION:3.0\nN:{nom};;;;\nTEL:{numero}\nEND:VCARD\n"
    
    # Ajout du contenu de la vCard au contenu global
    listes_de_tous_les_contacts += contenu_d_un_contact

# Chemin du fichier où nous allons écrire les vCards
filename = "C:/Users/Rab/Documents/all_contacts.vcf"

# Ouverture du fichier en mode écriture et écriture du contenu des vCards
with open(filename, "w") as vcf_file:
    vcf_file.write(listes_de_tous_les_contacts)  # Écriture des vCards dans le fichier