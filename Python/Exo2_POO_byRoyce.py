# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 03:55:14 2023

@author: Royce
"""
from datetime import datetime
#Création d'une classe Python nommée CompteBancaire qui représente un compte bancaire, ayant pour attributs : numeroCompte (type numérique ) , nom (nom du propriétaire du compte du type chaine), solde.

class CompteBancaire:
    histv = []  # historique des versements
    histr = []  # historique des retraits
    nbv=0 #nombre de versements
    nbr=0 #nombre de retraits
#2-Création d' un constructeur ayant comme paramètres : numeroCompte, nom, solde.
    def __init__(self,numeroCompte, nom, solde):
        self.__numeroCompte = numeroCompte
        self.__nom = nom.upper()
        if isinstance(solde, float) or isinstance(solde, int):
            if solde>0:            
                self.__solde = solde
            else:
                raise TypeError("Le solde doit être positive")
            
        else:
            raise TypeError("Le solde doit être numérique")
        
#3-Création d' une méthode Versement() qui gère les versements
    
    def versement(self, credit):
        if isinstance(credit, float) or isinstance(credit, int):
            if credit>0 :
                self.__solde += credit
                CompteBancaire.nbv += 1 
                date=datetime.now()
                date = date.strftime("%Y-%m-%d %H:%M:%S")
                CompteBancaire.histv.append((CompteBancaire.nbv, date, credit))
            else:
                raise TypeError("Le crédit doit être positive")
      
        else:
            raise TypeError("Le crédit doit être numérique")
            
            
#Création d'une méthode Retrait() qui gère les retraits.           

    def retrait(self,debit):
        if isinstance(debit, float) or isinstance(debit, int):

            if debit >0:                
                if debit < self.__solde :
                    CompteBancaire.nbr+=1
                    date=datetime.now()
                    date = date.strftime("%Y-%m-%d %H:%M:%S")
                    CompteBancaire.histr.append((CompteBancaire.nbr, date, debit))
                else:
                    raise TypeError("Le debit doit être inférieur au solde")
            else:
                raise TypeError("Le debit doit être positif")

        else:
            raise TypeError("Le debit doit être numérique")

#5-Création d' une méthode Agios() permettant d’appliquer les agios à un pourcentage de 5 % du solde
    def agios(self):
        self.__solde =self.__solde*95/100
        
#6-Création d' une méthode infos() permettant d’afficher les détails sur le compte

    @property
    def infos(self):
        print("Voici les détails de votre compte: ")
        print(f"N° du Compte: {self.__numeroCompte}")
        print(f"Nom: {self.__nom}")
        print(f"Historique des versements: {CompteBancaire.histv}")
        print(f"Historique des retraits: {CompteBancaire.histr}")
        print(f"Solde: {self.__solde}")
        
        


#Vérification      
mon_compte=CompteBancaire(155666395, "dupuiso", 1000)
mon_compte.versement(500)
mon_compte.versement(400)
mon_compte.retrait(900)
mon_compte.versement(500)

mon_compte.infos