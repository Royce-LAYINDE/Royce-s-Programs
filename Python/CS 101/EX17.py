# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 00:37:33 2023

@author: Royce
"""

def valider_parentheses(chaine):
    stack = []
    parentheses_ouvrantes = ['(', '[', '{']
    parentheses_fermantes = [')', ']', '}']
    parentheses_match = {'(': ')', '[': ']', '{': '}'}

    for caractere in chaine:
        if caractere in parentheses_ouvrantes:
            stack.append(caractere)
        elif caractere in parentheses_fermantes:
            if not stack:
                return False
            parenthese_ouverte = stack.pop()
            if parentheses_match[parenthese_ouverte] != caractere:
                return False

    return len(stack) == 0
chaine = "(([]))"
print(valider_parentheses(chaine))  # True

chaine = "(([{]}"
print(valider_parentheses(chaine))  # False
