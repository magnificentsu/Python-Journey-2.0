from PIL import Image, ImageFilter

img = Image.open('astro.jpeg')

new_img = img.resize((400, 200))
new_img.save('astro_thumbnail.jpeg')

img.thumbnail((400, 400))
img.save('astro_thumbnail2.jpeg')

