import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Chargement des jeux de données scrappées grâce à WebScrapper et BeautifulSoup
df_webscraper_voitures = pd.read_csv('expatdakar-voitures.csv')
df_webscraper_motos = pd.read_csv('expatdakar-moto.csv')
df_webscraper_equipment = pd.read_csv('expatdakr-equipement.csv')

df_beautifulsoup_voitures = pd.read_csv('voitures_a_vendre_data.csv')
df_beautifulsoup_motos = pd.read_csv('motos_scooters_a_vendre_data.csv')
df_beautifulsoup_equipment = pd.read_csv('equipements-pieces_a_vendre_data.csv')

st.write("-"*3)
# Logo
logo = 'Logo_DIT.png'
logo1 = 'logo-social.png'
    #centrons le logo
col1, col2, col3 = st.columns(3) 
with col1 : 
    st.image(logo, width=300) 
with col2 : 
    st.write("")
with col3 : 
    st.image(logo1, width=300)

st.write("-"*3)

# Page d'accueil
st.title("Banque de données scrappées sur le site Expat Dakar")
choix = st.radio("Choisissez la méthode de scrapping :", ("WebScrapper", "BeautifulSoup"))

st.write("-"*3)

# Si l'utilisateur choisit BeautifulSoup
if choix == "BeautifulSoup":
    choix_catégorie = st.selectbox("Choisissez la catégorie de données :", ("Voitures", "Motos", "Équipements"))

    # Affiche les données en fonction de la catégorie
    if choix_catégorie == "Voitures":
        st.write("Données scrappées avec BeautifulSoup sur des Voitures")
        st.dataframe(df_beautifulsoup_voitures)


    # Bouton "Visualiser les Graphiques"
        if st.button("Visualiser les Graphiques"):
            # Graphique 1 : Histogramme des Années
            st.title("Distribution des Années des Voitures")
            plt.hist(df_beautifulsoup_voitures['annee'], bins=[2000,2005,2010,2015,2020,2025], edgecolor='black')
            plt.xlabel('Année')
            plt.ylabel('Nombre de Voitures')
            st.pyplot(plt)

            # Graphique 2 : Nuage de Points Prix vs Année
            st.title("Nuage de Points Prix vs Année des Voitures")
            plt.figure(figsize=(8, 4))
            plt.scatter(df_beautifulsoup_voitures['annee'], df_beautifulsoup_voitures['prix'], alpha=0.5)
            plt.xlabel('Année')
            plt.ylabel('Prix')
            st.pyplot(plt)


    elif choix_catégorie == "Motos":
        st.write("Données scrappées avec BeautifulSoup sur des Motos")
        st.dataframe(df_beautifulsoup_motos)

        # Bouton "Visualiser les Graphiques"
        if st.button("Visualiser les Graphiques"):
            # Graphique 1 : Histogramme des Années des Motos
            st.title("Distribution des Années des Motos")
            plt.hist(df_beautifulsoup_motos['annee'], bins=[2000,2005,2010,2015,2020,2025], edgecolor='black')
            plt.xlabel('Année')
            plt.ylabel('Nombre de Motos')
            st.pyplot(plt)

            # Graphique 2 : Nuage de Points Prix vs Année des Motos
            st.title("Nuage de Points Prix vs Année des Motos")
            plt.figure(figsize=(8, 4))
            plt.scatter(df_beautifulsoup_motos['annee'], df_beautifulsoup_motos['prix'], alpha=0.5)
            plt.xlabel('Année')
            plt.ylabel('Prix')
            st.pyplot(plt)

    elif choix_catégorie == "Équipements":
        st.write("Données scrappées avec BeautifulSoup sur des Équipements")
        st.dataframe(df_beautifulsoup_equipment)

        # Bouton "Visualiser les Graphiques"
        if st.button("Visualiser les Graphiques"):
            # Graphique 1 : Diagramme en batons pour les Détails
        # Graphique 1 : Distribution des Articles par Localités
            st.title("Distribution des Articles par Localités")
            st.bar_chart(df_beautifulsoup_equipment['localite'].value_counts(),color='#000000')


            # Graphique 2 : Distribution des Prix des Équipements
            st.title("Distribution des Prix des Équipements")
            plt.figure(figsize=(8, 4))
            plt.hist(df_beautifulsoup_equipment['prix'], bins=[0, 5000, 10000, 50000, 100000, 200000], edgecolor='black')
            # plt.xscale('log')  # Échelle logarithmique pour mieux visualiser les différences
            plt.xlabel('Prix')
            plt.ylabel('Nombre d\'Articles')
            st.pyplot(plt)



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


st.write("-"*3)
col4,col5 = st.columns(2)
with col4:
    st.write("Réalisé par Malick Royce & Mouhamed DIOP")
with col5:
    st.write("Sous la supervision de M. Wahab DIALLO")
st.write("-"*3)