# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 15:24:14 2023

@author: Royce
"""
def palindrome(lemot):
    for i,j in zip(reversed(lemot),lemot):
        if i!=j:
            return False                       
    return True
    

print(palindrome("anana"))