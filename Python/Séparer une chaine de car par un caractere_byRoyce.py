# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 03:17:40 2023

@author: Royce
"""
a=str(input("entre le mot: "))

#METHODE1
print('*'.join(a))


####ou


car="*"
new_a=a[0]

i=1
while i < len(a):
    new_a=new_a + car + a[i]
    i=i+1
print(new_a)