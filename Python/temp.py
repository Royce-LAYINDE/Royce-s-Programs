# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("Hello world")
import matplotlib.pyplot as plt
plt.grid(True)
f = open("C:\\Users\\ndour\\OneDrive\\Documents\\Cours\\python\\dataset.txt")
X = []
Y = []
for line in f.readlines():
    # diviser la ligne
    l=line.split("\t")
    # recuperer X
    x = l[0]
    # recup Y
    y = l[1]
    # nettoyer X
    if x!="X" and y!="Y":
        x = int(x)
    # nettoyer Y
        y = float(y)
    # stocker X
        X.append(x)
    # stocker Y
        Y.append(y)

plt.scatter(X,Y, c = 'r')
plt.show()

M_X = sum(X) / len(X)
print(M_X)
l1=[1,2,200,203,204]
m1 = sum(l1)/len(l1)
i = (len(l1) - 1) // 2
m2 = l1[i]
print(m1)
print(m2)