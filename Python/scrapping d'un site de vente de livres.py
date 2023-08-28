# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 09:33:42 2023

@author: Royce
"""
#ici on souhaite recuperer sur un site de vente de livres, uniquement les titres des 40 premiers livres et leur prix

#PHASE DE PREPARATION

##On importe les modules nécessaires
import re
from urllib.request import urlopen


#On stocke les liens dans des variables
#Etant donné qu'on doit recuperer les 40 premiers résultats et qu'une page du site ne contient que 20 résultats alors on aura 2 pages à scraper
url_page1 = "https://books.toscrape.com/"
url_page2 = "https://books.toscrape.com/catalogue/page-2.html"

# On telecharge les documents html grace à une fonction
# Puis on les sauvegarde dans un fichier sur notre pc
    ##Création de la fonction
def download_html_document(lien,repertoire):
    doc = urlopen(lien).read().decode()
    f = open(repertoire, "w")
    f.write(doc)
    print("Votre document html a été telechargé avec succes")
    f.close()


#On procède maintenant à l'extraction des données
    ##Création de la fonction
def extract(fichier_en_entré,fichier_en_sortie):
    f = open(fichier_en_entré, "r")
    html = f.read()
    
    ##Grace au regex, on recupere uniquement les titres des livres sur la page
    titres_des_livres = re.findall(r'<h3><a.*?>(.*?)</a></h3>', html)
    # for titre in titres_des_livres:
    #    print(titre)
       
    ##Grace au regex, on recupere uniquement les prix unitaires des livres sur la page
    prix_des_livres = re.findall(r'<p class="price_color">(.*?)</p>', html)
    # for prix in prix_des_livres:
    #     print(prix)
        
    ##On sauvegarde le tout dans un fichier texte
    with open(fichier_en_sortie, "w") as file:
        for titre, prix in zip(titres_des_livres, prix_des_livres):
            file.write(f"Titre : {titre}\n")
            file.write(f"Prix unitaire en £ : {prix}\n")
            file.write("\n")

    print("Les titres et les prix des livres ont été enregistrés dans le fichier texte comme vous le vouliez.")


    f.close()
    
#PHASE D'APPLICATION 
  
    ##Sauvegarde des pages
download_html_document(url_page1,"./page1.html")
download_html_document(url_page2,"./page2.html")

    ##Extraction proprement dite 
extract("./page1.html","./Page1.txt")
extract("./page2.html","./Page2.txt")