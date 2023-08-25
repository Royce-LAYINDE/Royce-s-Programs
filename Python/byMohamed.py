points = "0,1; 2,17; 3,34; 6,21; 10,321; 14,617; 16,801; 20,1000; 22,1500"

A= points.split(";")

x = []
y = []

for i in A:
    
    nombre_x,nombre_y = i.split(",") 
    x.append(int(nombre_x)+1 )  
    y.append(int(nombre_y))
print("Liste x :", x)
print("Liste y :", y)
