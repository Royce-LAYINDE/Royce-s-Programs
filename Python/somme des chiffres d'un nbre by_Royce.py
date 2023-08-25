# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 16:55:42 2023

@author: Royce
"""
r=0
n=1245
while n!=0:
    n=n // 10
    x=n%10
    r+=x
print(r)