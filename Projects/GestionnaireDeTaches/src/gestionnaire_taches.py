from datetime import datetime
from tache import Tache

class GestionnaireTaches:
    def __init__(self):
        # Initialisation de la liste des tâches
        self.taches = []

    def ajouter_tache(self, tache):
        # Méthode pour ajouter une nouvelle tâche à la liste
        self.taches.append(tache)

    def supprimer_tache(self, titre_tache):
        # Méthode pour supprimer une tâche de la liste par son titre
        self.taches = [tache for tache in self.taches if tache.titre != titre_tache]

    def obtenir_taches(self, statut=None):
        # Méthode pour obtenir toutes les tâches ou filtrer par statut si spécifié
        if statut:
            return [tache for tache in self.taches if tache.statut.lower() == statut.lower()]
        else:
            return self.taches

    def afficher_taches(self, taches=None):
        # Méthode pour afficher les détails des tâches, peut afficher une liste spécifique si fournie
        taches_a_afficher = taches if taches else self.taches
        for tache in taches_a_afficher:
            print(f"titre: {tache.titre}, Date d'échéance: {tache.date_echeance}, Priorité: {tache.priorite}, Statut: {tache.statut}")

    def rechercher_tache(self, titre_tache):
        # Méthode pour rechercher des tâches par titre
        return [tache for tache in self.taches if titre_tache.lower() in tache.titre.lower()]

    def trier_taches(self, critere):
    # Méthode pour trier les tâches en fonction du critère spécifié
        if critere == "statut":
            self.taches.sort(key=lambda x: x.statut)
        elif critere == "priorite":
            self.taches.sort(key=lambda x: x.priorite, reverse=True)
        elif critere == "date":
            self.taches.sort(key=lambda x: x.date_echeance)