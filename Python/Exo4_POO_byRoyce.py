# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 22:04:43 2023

@author: Royce
"""

#1 - Créer une classe Calcul ayant un constructeur par défaut (sans paramètres) permettant d'eectuer diérents calculs sur les nombres entiers

class Calcul:
   
#2 - Créer au sein de la classe Calcul une méthode nommée Factorielle() qui permet de calculer le factorielle d'un entier. 

    def factorielle(self,n):
        f=1
        i=1
        while i< n +1:
            f*=i
            i+=1
        return f

#Tester la méthode en faisant une instanciation sur la classe
 
# mon_calcul=Calcul()
# print(mon_calcul.factorielle(3))   

#3 - Créer au sein de la classe Calcul une méthode nommée Somme() permettant de calculer la somme des n premiers entiers 1+2+3+..+n. 

    def somme(self,n):
        
        s=0
        i=n
        while i>0:
            s+=i
            i-=1
        return s
        

#Tester la méthode

# mon_calcul=Calcul()
# print(mon_calcul.somme(5)) 

#4 - Créer au sein de la classe Calcul une méthode nommée testPrim() permettant de tester la primalité d'un entier donné 

    def testPrim(self,n):
        
        if  n==1:
            return(f"{n} n'est pas un nombre premier")
        elif n==2:
            return(f"{n} est  un nombre premier")
        else:
            for i in range(2,n):
                if n%i==0:
                    return(f"{n} n'est pas un nombre premier")
            return(f"{n} est  un nombre premier")

#Tester la méthode

# mon_calcul=Calcul()
# print(mon_calcul.testPrim(2))

#4 - Créer au sein de la classe Calcul une méthode nommée testPrims() permettant de tester si deux nombres sont premier entre eux

    def testPrims(self,x,y):
        
        a=x if x < y else y
        for i in range(2,a+1):
            if x%i == 0 and y%i == 0:
                return f"{x} et {y} ne sont pas premiers entre eux"
                
        return f"{x} et {y} sont premiers entre eux"
    

# #Tester la méthode 

# mon_calcul=Calcul()
# print(mon_calcul.testPrims(14,7))

#5 - Créer une méthode tableMult() qui crée et affiche la table de multiplication d'un entier donné. 

    def tableMult(self,n,end):
        
        for e in range(0,end+1):
            print(f"{n} * {e} = {n*e}")

# #Tester la méthode 

# mon_calcul=Calcul()
# mon_calcul.tableMult(5,16)

#Créer ensuite une méthode allTablesMult() permettant d'afficher toutes les tables de multiplications des entiers 1, 2, 3, ..., 9.

    def allTablesMult(self,end):
        
        for i in range(2,10):
            print(f"Table de {i}")
            for e in range(0,end+1):
                
                print(f"{i} * {e} = {i*e}")
        
# #Tester la méthode 

# mon_calcul=Calcul()
# mon_calcul.allTablesMult(7)      

#6 - Créer une méthode statique listDiv() qui récupère tous les diviseurs d'un entier donné sur une liste Ldiv.

    @staticmethod
    def listDiv(n):
        Ldiv=[]
        for i in range(1,n+1):
            if n%i==0:
                Ldiv.append(i)
        return Ldiv

#Tester la méthode 

# print(Calcul.listDiv(10))

#Créer une autre méthode listDivPrim() qui récupère tous les diviseurs premiers d'un entier donné.

    @staticmethod
    def listDivPrim(n):
        LdivPrim=[]
        for i in range(1,n+1):
            if n%i==0: 
                if i==1:
                    continue
                elif i==2:
                   LdivPrim.append(i)                   
                else:
                    v=True
                    for e in range(2,i):
                        if i%e==0:
                            v=False
                            continue
                    if v==True:
                        LdivPrim.append(i)
                       
                        
                        
                        
        return LdivPrim

#Tester la méthode 

print(Calcul.listDivPrim(21))











