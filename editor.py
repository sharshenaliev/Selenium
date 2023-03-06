from PIL import Image

def edit():
    image = Image.open('image.png')
    image = image.crop((0, 0, 340, 195))
    image.save('captcha.png')
