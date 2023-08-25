Note=[10.5,15.5,20,7,9.5]
a=0
for i,e in enumerate(Note):
    if i==1:
        e=2*e
    elif i==3:
        e=3*e
    else:
        e=e
    a=a+e


print("La somme est:",a)
M=a/(len(Note)+3)
print("La moyenne est: ",M)
