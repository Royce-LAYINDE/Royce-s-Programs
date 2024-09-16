from flask import Flask, render_template, request, redirect, url_for
from src.gestionnaire_taches import *
from tache import *

app = Flask(__name__)
gestionnaire = GestionnaireTaches()

# Route pour la page d'accueil
@app.route('/')
def accueil():
    taches = gestionnaire.obtenir_taches()
    return render_template('index.html', taches=taches)

# Route pour ajouter une nouvelle tâche
@app.route('/ajouter_tache', methods=['POST'])
def ajouter_tache():
    titre = request.form['titre']
    date_echeance = request.form['date_echeance']
    description = request.form.get('description', '')
    gestionnaire.ajouter_tache(Tache(titre, date_echeance, description))
    return redirect(url_for('accueil'))

# Route pour supprimer une tâche
@app.route('/supprimer_tache/<titre_tache>', methods=['GET'])
def supprimer_tache(titre_tache):
    gestionnaire.supprimer_tache(titre_tache)
    return redirect(url_for('accueil'))

# Route pour afficher toutes les tâches
@app.route('/toutes_taches', methods=['GET'])
def toutes_taches():
    taches = gestionnaire.obtenir_taches()
    return render_template('index.html', taches=taches)

# Route pour afficher les tâches en cours
@app.route('/taches_en_cours', methods=['GET'])
def taches_en_cours():
    taches = gestionnaire.obtenir_taches(statut="En cours")
    return render_template('index.html', taches=taches)

# Route pour afficher les tâches terminées
@app.route('/taches_terminees', methods=['GET'])
def taches_terminees():
    taches = gestionnaire.obtenir_taches(statut="Terminé")
    return render_template('index.html', taches=taches)

# Route pour rechercher une tâche
@app.route('/rechercher_tache', methods=['POST'])
def rechercher_tache():
    titre_tache = request.form['titre_tache']
    taches = gestionnaire.rechercher_tache(titre_tache)
    return render_template('index.html', taches=taches)

# Route pour trier les tâches
@app.route('/trier_taches/<critere>', methods=['GET'])
def trier_taches(critere):
    gestionnaire.trier_taches(critere)
    return redirect(url_for('accueil'))

if __name__ == '__main__':
    app.run(debug=True)
