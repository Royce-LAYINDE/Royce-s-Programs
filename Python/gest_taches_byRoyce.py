from datetime import datetime
import easygui

class GestionTaches:
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, titre, description, statut):
        date_ajout = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tache = {"titre": titre, "description": description, "statut": statut, "date_ajout": date_ajout}
        self.taches.append(tache)

    def afficher_taches(self):
        return self.taches

class InterfaceLigneCommande:
    def __init__(self, gestionnaire_taches):
        self.gestionnaire_taches = gestionnaire_taches

    def afficher_menu(self):
        while True:
            choix = input("Sélectionnez une option (1. Afficher Tâches, 2. Ajouter Tâche, 3. Quitter): ")

            if choix == "1":
                taches = self.gestionnaire_taches.afficher_taches()
                print("Liste des Tâches:")
                for i, tache in enumerate(taches, start=1):
                    print(f"{i}. {tache['titre']} - {tache['statut']}")
            elif choix == "2":
                titre = input("Entrez le titre de la tâche: ")
                description = input("Entrez la description de la tâche: ")
                statut = input("Choisissez le statut de la tâche (À faire, En cours, Terminée): ")
                self.gestionnaire_taches.ajouter_tache(titre, description, statut)
                print("Tâche ajoutée avec succès!")
            elif choix == "3":
                break
            else:
                print("Option non valide. Veuillez réessayer.")

class InterfaceEasyGui:
    def __init__(self, gestionnaire_taches):
        self.gestionnaire_taches = gestionnaire_taches

    def afficher_menu(self):
        while True:
            choix = easygui.buttonbox("Sélectionnez une option:", choices=["Afficher Tâches", "Ajouter Tâche", "Quitter"])

            if choix == "Afficher Tâches":
                taches = self.gestionnaire_taches.afficher_taches()
                tache_str = "\n".join([f"{i+1}. {tache['titre']} - {tache['statut']}" for i, tache in enumerate(taches)])
                easygui.msgbox(f"Liste des Tâches:\n\n{tache_str}", title="Tâches")
            elif choix == "Ajouter Tâche":
                titre = easygui.enterbox("Entrez le titre de la tâche:")
                description = easygui.enterbox("Entrez la description de la tâche:")
                statut = easygui.choicebox("Choisissez le statut de la tâche:", choices=["À faire", "En cours", "Terminée"])
                self.gestionnaire_taches.ajouter_tache(titre, description, statut)
                easygui.msgbox(f"Tâche ajoutée avec succès!\n\nTitre: {titre}\nDescription: {description}\nStatut: {statut}")
            elif choix == "Quitter":
                break

# Créer une instance de GestionTaches
gestionnaire_taches = GestionTaches()

# Choisir le contexte (ligne de commande ou easygui)
contexte = input("Choisissez le contexte (1. Ligne de commande, 2. EasyGui): ")

if contexte == "1":
    interface = InterfaceLigneCommande(gestionnaire_taches)
elif contexte == "2":
    interface = InterfaceEasyGui(gestionnaire_taches)
else:
    print("Option non valide. Quitter.")

# Afficher le menu selon le contexte choisi
if contexte in ["1", "2"]:
    interface.afficher_menu()

#---------------------------------------------------------------------------------------------------------------

# import streamlit as st
# from datetime import datetime

# class GestionTaches:
#     def __init__(self):
#         self.taches = []

#     def ajouter_tache(self, titre, description, statut):
#         date_ajout = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         tache = {"titre": titre, "description": description, "statut": statut, "date_ajout": date_ajout}
#         self.taches.append(tache)

#     def afficher_taches(self):
#         return self.taches

# def main():
#     st.title("Gestionnaire de Tâches avec Streamlit")

#     gestionnaire_taches = GestionTaches()

#     i = 0  # Counter for dynamic keys
#     i < 1
#     while True:
#         i += 1  # Increment the counter
#         choix = st.radio("Sélectionnez une option:", ["Afficher Tâches", "Ajouter Tâche", "Quitter"], key=f"main_radio_{i}")

#         if choix == "Afficher Tâches":
#             taches = gestionnaire_taches.afficher_taches()
#             st.text("Liste des Tâches:")
#             for i, tache in enumerate(taches, start=1):
#                 st.text(f"{i}. {tache['titre']} - {tache['statut']}")
#         elif choix == "Ajouter Tâche":
#             titre = st.text_input("Entrez le titre de la tâche:", key=f"add_title_{i}")
#             description = st.text_area("Entrez la description de la tâche:", key=f"add_description_{i}")
#             statut = st.selectbox("Choisissez le statut de la tâche:", ["À faire", "En cours", "Terminée"], key=f"add_status_{i}")
#             gestionnaire_taches.ajouter_tache(titre, description, statut)
#             st.success("Tâche ajoutée avec succès!")
#         elif choix == "Quitter":
#             break

# if __name__ == "__main__":
#     main()
