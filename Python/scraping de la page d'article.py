# Importer les outils magiques
import urllib.request
from bs4 import BeautifulSoup

# L'URL de la page à explorer
url = "https://roylab.netlify.app/fr/first"

doc = urllib.request.urlopen(url)  # Invoquer la page avec notre sort d'invocation (urllib)

contenu = BeautifulSoup(doc, "html.parser")   # Utilisation de Beautiful Soup pour analyser le contenu HTML de la page


# Obtenir le contenu HTML formaté
contenu_html = contenu.prettify()

# Sauvegarder le contenu HTML dans un fichier
nom_du_fichier = "page.html"
with open(nom_du_fichier, "w", encoding="utf-8") as file:
    file.write(contenu_html)

print(f"✨ Le contenu HTML de la page a été sauvegardé dans: {nom_du_fichier}")


# Trouver tous les éléments <a> qui contiennent des liens
links = contenu.find_all("a")

# Trouver le titre de l'article avec notre sort de divination (Beautiful Soup)
title = contenu.find("h1").text

# Afficher les liens sécurisés trouvés avec un geste d'enchantement
print("🔮 Voici la liste des liens sécurisés trouvés sur cette page:")
for link in links:
    href = link.get("href")     # Extraire l'attribut "href" de la balise <a> pour obtenir le lien
    if href and href.startswith("https"):   # Filtrer les liens pour ne prendre en compte que ceux commençant par "https"
        print(href)

# Afficher le titre de l'article pour captiver l'attention
print(f"📜 Titre de l'article : {title}")
