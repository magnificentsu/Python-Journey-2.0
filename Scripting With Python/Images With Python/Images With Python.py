from PIL import Image, ImageFilter

img = Image.open('Pokedex/pikachu.jpeg')

print(img.format) #give image format
print(img.size) #gives image size
print(img.mode) #gives coloring of image(rgb)
# print(dir(img)) #see all you get with image

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blur.png', 'png')

filtered_img2 = img.convert('L')
filtered_img2.save('grey.png', 'png')

filtered_img3 = filtered_img2.rotate(180)
filtered_img3.save('crooked_grey.png', 'png')
filtered_img3.show()

filtered_img4 = filtered_img2.resize((300, 300))
filtered_img4.save('small_grey.png', 'png')

box = (100, 100, 400, 400)
fileterd_img5 = filtered_img2.crop(box)
fileterd_img5.save('cropped_grey.png', 'png')

