import streamlit as st
import pandas as pd

# Chargement des jeux de données scrappées grace à webscrapper et beautifulSoup
df_webscraper_voitures = pd.read_csv('motos_scooters_a_vendre_data.csv')
df_webscraper_motos = pd.read_csv('motos_scooters_a_vendre_data.csv')
df_webscraper_equipment = pd.read_csv('motos_scooters_a_vendre_data.csv')

df_beautifulsoup_voitures = pd.read_csv('voitures_a_vendre_data.csv')
df_beautifulsoup_motos = pd.read_csv('motos_scooters_a_vendre_data.csv')
df_beautifulsoup_equipment = pd.read_csv('equipements-pieces_a_vendre_data.csv')

# Logo
logo = 'Logo_DIT.png'
st.image(logo, width=200) 


# Page d'accueil
st.title("Banque de données scrappées sur le site Expats Dakar")
choix = st.radio("Choisissez la méthode de scrapping :", ("WebScrapper", "BeautifulSoup"))

# Si l'utilisateur choisit BeautifulSoup
if choix == "BeautifulSoup":
    choix_catégorie = st.selectbox("Choisissez la catégorie de données :", ("Voitures", "Motos", "Équipements"))

    # Affiche les données en fonction de la catégorie
    if choix_catégorie == "Voitures":
        st.write("Données scrappées avec BeautifulSoup sur des Voitures")
        st.dataframe(df_beautifulsoup_voitures)

    elif choix_catégorie == "Motos":
        st.write("Données scrappées avec BeautifulSoup sur des Motos")
        st.dataframe(df_beautifulsoup_motos)

    elif choix_catégorie == "Équipements":
        st.write("Données scrappées avec BeautifulSoup - Équipements")
        st.dataframe(df_beautifulsoup_equipment)

# Si l'utilisateur choisit WebScrapper
else:
    choix_catégorie1 = st.selectbox("Choisissez la catégorie de données :", ("Voitures", "Motos", "Équipements"))

    # Affiche les données en fonction de la catégorie
    if choix_catégorie1 == "Voitures":
        st.write("Données scrappées avec webscraper sur des Voitures")
        st.dataframe(df_webscraper_voitures)

    elif choix_catégorie1 == "Motos":
        st.write("Données scrappées avec webscraper sur des Motos")
        st.dataframe(df_webscraper_motos)

    elif choix_catégorie1 == "Équipements":
        st.write("Données scrappées avec webscraper - Équipements")
        st.dataframe(df_webscraper_equipment)