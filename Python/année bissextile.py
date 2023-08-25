année=int(input("Veuillez entrer l'année à vérifié"))
if (année%4==0 and année%100!=0 ) or (année%400==0):
    print("L'année", année, "est une année bissextile")
else:
        print("L'année",année, "n'est pas une année bissextile")
