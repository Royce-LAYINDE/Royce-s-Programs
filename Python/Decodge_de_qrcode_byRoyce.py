#s'assurer d'avoir installer la bibliotheque qrcode avec pip install pyzbar
from pyzbar.pyzbar import decode
#s'assurer d'avoir installer la bibliotheque pillow avec pip install pillow
from PIL  import Image
#s'assurer d'avoir deja un qrcode a l'adresse renseignée
img = Image.open('C:/Users/lenovo/Documents/qrcode.png')
result = decode(img)
print(result)