# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 15:29:59 2023

@author: Royce
"""
# D�finition de la classe
class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        
    def afficher_info(self):
        print("Marque :", self.marque)
        print("Mod�le :", self.modele)
        print("Ann�e :", self.annee)

# Appel de la classe pour cr�er une instance
ma_voiture = Voiture("Toyota", "Camry", 2020)

# Utilisation de l'instance pour appeler une méthode
ma_voiture.afficher_info()
