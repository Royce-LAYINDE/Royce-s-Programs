# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 16:41:10 2023

@author: lenovo
"""

def operateur(op,a,b):
    def addition(x,y):
        return x+y
    def soustraction(z,r):
        return z-r
    if op=="+":
        return addition(a,b)
    elif op=="-":
        return soustraction(a,b)
    
    else:
        print("Erreur")
    
    