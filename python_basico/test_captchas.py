from PIL import Image # Importando o módulo Pillow para abrir a imagem no script

import pytesseract # Módulo para a utilização da tecnologia OCR
path = r'C:\Users\reiload\PycharmProjects\udemy_my_course\python_basico\test.jpg'

# Extraindo o texto da imagem
print(pytesseract.image_to_string(Image.open(path), lang='por'))
