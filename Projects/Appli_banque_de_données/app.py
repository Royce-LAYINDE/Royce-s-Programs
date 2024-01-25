import streamlit as st
import pandas as pd

# Chargement des jeux de données extraits avec web scrapper et beautifulSoup
df_webscraper_voitures = pd.read_csv('voitures_a_vendre_data.csv')  
df_webscraper_motos = pd.read_csv('motos_scooters_a_vendre_data.csv')
df_webscraper_equipment = pd.read_csv('equipements-pieces_a_vendre_data.csv')

# df_beautifulsoup_voitures = pd.read_csv('voitures_a_vendre_data.csv')
# df_beautifulsoup_motos = pd.read_csv('motos_scooters_a_vendre_data.csv')  
# df_beautifulsoup_equipment = pd.read_csv('equipements-pieces_a_vendre_data.csv')  
 

# Initialisation de l'nterface utilisateur
st.title("Banque de données scrappées sur le site Expats Dakar")

# Création des boutons pour télécharger les données

# Boutons pour accéder aux données scrappées avec Web scrapper
if st.button("Accéder aux données scrappées avec Web Scrapper"):
    st.subheader("Sélectionnez sur quoi voulez-vous avoir un jeu de données")
    options = ['Voitures', 'Motos', 'Equipements']
    choix = st.selectbox('', options)
    if choix == "Voitures":
        st.write(df_webscraper_voitures)
    if choix == "Motos":
        st.write(df_webscraper_motos)
    if choix == "Equipements":
        st.write(df_webscraper_equipment)


# Boutons pour accéder aux données scrappées avec Beautiful Soup
# if st.button("Accéder aux données scrappées avec Beautiful Soup"):
#     st.subheader("Sélectionnez sur quoi voulez-vous avoir un jeu de données")
#     options = ['Voitures', 'Motos', 'Equipements']
#     choix_bs = st.selectbox('', options)
#     if choix_bs == "Voitures":
#         st.write(df_beautifulsoup_voitures)
#     elif choix_bs == "Motos":
#         st.write(df_beautifulsoup_motos)
#     elif choix_bs == "Équipements":
#         st.write(df_beautifulsoup_equipment)

# Bouton pour visualiser des graphes sur le jeu de données Beautiful Soup
if st.button("Visualiser des graphes sur le jeu de données Beautiful Soup"):
    st.subheader("Graphes sur le jeu de données Beautiful Soup")
