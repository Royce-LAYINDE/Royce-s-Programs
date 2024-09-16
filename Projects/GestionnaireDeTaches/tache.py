from datetime import datetime


class Tache:
    def __init__(self, titre, date_echeance, description="", priorite=False, statut="A faire"):
        self.titre = titre
        self.date_echeance = datetime.strptime(date_echeance, '%Y-%m-%d')
        self.description = description
        self.statut = statut