#s'assurer d'avoir installer la bibliotheque qrcode avec pip install pyzbar
from pyzbar.pyzbar import decode
#s'assurer d'avoir installer la bibliotheque pillow avec pip install pillow
from PIL  import Image
#s'assurer d'avoir deja un qrcode a l'adresse renseignée
img = Image.open('myfirst_qrcode.png')
resultat = decode(img)
# print(type(resultat))
# print(resultat)

for information in resultat:
    # Extraire et afficher le type du code (généralement 'QRCODE')
    code_type = information.type
    print(f"Type de code : {code_type}")

    # Extraire et afficher les données du code
    data = information.data.decode('utf-8')  # Décode les données du code QR
    print(f"Données du code : {data}")

    # Extraire et afficher la taille du QR code (en pixels)
    rect = information.rect  # Récupérer les coordonnées du rectangle du code QR
    width = rect.width  # Largeur du rectangle
    height = rect.height  # Hauteur du rectangle
    print(f"Taille du code (en pixels) - Largeur : {width}, Hauteur : {height}")
    # Extraire et afficher la qualité du décodage
    qualite_decodage = information.quality
    print(f"Qualité de décodage : {qualite_decodage}")
    # Extraire et afficher l'orientation du QR code'
    code_orientation = information.orientation
    print(f"Orientation du qr code : {code_orientation}")

