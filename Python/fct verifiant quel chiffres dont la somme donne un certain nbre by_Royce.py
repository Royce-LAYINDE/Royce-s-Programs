# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 15:29:59 2023

@author: Royce
"""

def num_cible(nums,cible):

    r = []
    for i,e1 in enumerate(nums):
        for j,e2 in enumerate(nums):
            if e2 + e1 == cible:
                if e1 and e2 not in r:
                    return [i,j]
                    # r.extend([i,j])
    # return r

liste=[1,2,4]
p=num_cible(liste,6)
print(p)