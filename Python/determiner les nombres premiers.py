#Il faut juste changer les extrémités du premier range pour chercher les nombres premiers dans l'intervalle en question


for n in range(13, 900):
    for x in range(2, n):
        if n % x == 0:
            print(n, '=', x, '*', n//x)
            break
    else:
        # Si la boucle interne ne rencontre pas de break, cette ligne de code est exécutée pour afficher un message indiquant que n est un nombre premier.
        print(n, 'est un nombre premier')