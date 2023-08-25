# -*- coding: utf-8 -*-
"""

@author: Royce
"""
from fractions import Fraction

A =range(0,101)

N= set()
Z=set()
D=set()
Q=set()
Q1=set()
Q2=set()
R=set()

#Creation de N
for i in A:
    N.add(i)
#print("N=",N)

#Creation de Z
Z.update(N)
for i in N:
    Z.add(-i)
#print("Z=",Z)

#Creation de D
#NB: Le dernier élément de D sera 10 car 100/10 , 100 étant le dernier élément de notre A
D=D.union(Z)
for i in Z:
    for e in Z:
        if e!= 0:
            D.add(i/e)
#print("D=",D)


#Creation de Q  


Q=Q.union(D)
for i in Z:
    for e in range(1,101):
        q=Fraction(i,e)
        #print(q)
        Q.add(q)
#print("Q=",Q)

#Creation de R
R=R.union(Q)
#print("R=",R)

#Test d'appartenance

#De N dans Z

# for i in N:
#     if i in Z:
#         print(i,"trouver")        
#     else:
#         print(i,"pas trouver")

#De Z dans D

# for i in Z:
#     if i in D:
#         print(i,"trouver")
#     else:
#         print(i,"pas trouver")

#De Z dans Q

# for i in Z:
#     if i in Q:
#         print(i,"trouver")     
#     else:
#         print(i,"pas trouver")

# #De D dans Q

# for i in D:
#     if i in Q:
#         print(i,"trouver")     
#     else:
#         print(i,"pas trouver")

#De D dans R

# for i in D:
#     if i in R:
#         print(i,"trouver")
        
#     else:
#         print(i,"pas trouver")

#De Q dans R

# for i in Q:
#     if i in R:
#         print(i,"trouver")
        
#     else:
#         print(i,"pas trouver")
    



    
# if -35/3 in Q:
#     print("ok")
# else:
#     print("bad")


    

