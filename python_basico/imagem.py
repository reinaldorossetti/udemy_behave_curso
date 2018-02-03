from PIL import ImageEnhance, Image

path = r'C:\Users\reiload\PycharmProjects\udemy_my_course\python_basico\test.jpg'
image = Image.open(path)
enhancer = ImageEnhance.Sharpness(image)

for i in range(8):
    factor = i / 4.0
    enhancer.enhance(factor).show("Sharpness %f" % factor)