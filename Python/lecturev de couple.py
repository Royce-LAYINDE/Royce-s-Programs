# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
"""
Created on Fri Feb  3 11:05:50 2023

@author: o
"""
chemin="C:\\Users\\o\\Desktop\\mes cours\\python\\fichier etc\\dataset.txt"
fichier= open(chemin)
lignes=fichier.readlines()
lignes.pop(0)
print(lignes[2])
X=[]
Y=[]
for l in lignes:
    couple=l.split("\t")
    X.append(int(couple[0]))
    Y.append(float(couple[1].strip("\n")))
#print(X)
#print(Y)
#strip permet d'enlever des caracteres a l'estremité des chaine de caractère
fig, ax = plt.subplots()
ax.scatter(X,Y, c="green")


ax.set_xlabel("liste des x", fontsize=15)
ax.set_ylabel("listes des y", fontsize=15)
ax.set_title('liste des points')

ax.grid(True)
fig.tight_layout()

plt.show()
#pour les listes x et y, ecrire la fonction qui calcul le max (xmax et ymax) et le min (xmin, ymin)
#ecrire une fonction qui calcule la valeure moyenne et la valeure medianne d'une liste 
#ecrire la fonction qui calcule la variance d'une liste

def min_max(X):
    s=0
    m=X[0]
    M=X[0]
    for i in X:
        s=s+i
        moyenne=s/len(X) 
        if i<m:
            m=i
        elif i>M:
            M=i
                  
    return M,m,moyenne       

def median(X):
    data = sorted(X)
    index = len(data) // 2
    
  
    if len(X) % 2 != 0:
        return data[index]
    
   
    return (data[index - 1] + data[index]) / 2

def variance(l):
#calcul de la variance des valeurs d’une liste de nombres l’’’
   m=moyenne(l)
   v=0
   for k in range(0,len(l)):
        v=v+(l[k]-m)**2
   return(v/len(l))