# -*- coding: utf-8 -*-
"""
author: M.Royce
"""
# Chemin du fichier texte contenant les contacts
fichier_contacts = "C:/Users/Rab/Documents/G3contacts.txt"

# Initialisation de la variable qui contiendra toutes les vCards
listes_de_tous_les_contacts = ""

# Ouverture du fichier texte en mode lecture
with open(fichier_contacts, "r") as contacts_file:
    for ligne in contacts_file:
        # Séparation de la ligne en prénom, nom et numéro en utilisant la tabulation comme séparateur
        nom, prenom, numero = ligne.strip().split("\t")
        
        # Création du contenu d'une vCard pour le contact actuel
        contenu_d_un_contact = f"BEGIN:VCARD\nVERSION:3.0\nN:{prenom};{nom};;;\nTEL:{numero}\nEND:VCARD\n"
        
        # Ajout du contenu de la vCard au contenu global
        listes_de_tous_les_contacts += contenu_d_un_contact

# Chemin du fichier où nous allons écrire les vCards
filename = "C:/Users/Rab/Documents/all_contactsG7.vcf"

# Ouverture du fichier en mode écriture et écriture du contenu des vCards
with open(filename, "w") as vcf_file:
    vcf_file.write(listes_de_tous_les_contacts)  # Écriture des vCards dans le fichier
