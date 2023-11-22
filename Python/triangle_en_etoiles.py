def saisie():
    n = int(input("Entre un nombre"))
    return n

def triangle(n):
    for i in range(n+1):
        print("*" * i)