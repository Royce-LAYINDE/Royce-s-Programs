#Lecture d'un fichier a partir de son chemin sur le systeme d'exploitation
f = open("C:\\Users\\lenovo\\Documents\\DATA\\Python\\dataset.txt")
#Premiere maniere de lire le contenu du fichier
#contenu = f.read()
#Read recupere tout le contenu en une fois et au format str
#print(contenu)

#Deuxieme maniere de lire le contenu
contenu = f.readline()
print(contenu)
#Readline permet de lire une seule ligne a la fois
#le \n permet de definir la fin d'une ligne

# #Troisieme maniere de lire un fichier
# lignes = f.readlines()
# print(lignes)
# #Readlines permet de recuperer tout le contenu sous la forme d'une liste de str
# print(lignes [10])


