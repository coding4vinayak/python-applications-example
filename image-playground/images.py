# rotate, smooth , sharpen, show, resize, crop, 

from PIL import Image, ImageFilter


img =  Image.open("./astro.jpg")

print(img.size)

img.thumbnail((400, 200))

img.save('thumbnail.jpg')