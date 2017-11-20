# LEVEL 28
# http://www.pythonchallenge.com/pc/ring/bell.html
from PIL import Image

img = Image.open('data/bell.png')
R, G, B = 0, 1, 2
w, h = img.size
# w, h = 20, 20

print(img.mode)
print(img.size)
print(img.info)

# the picture shows vertical stripes, let's try the horizontal differences by pairs
for y in range(h):
    for x in range(0, w, 2):
        dif = abs(img.getpixel((x, y))[G] - img.getpixel((x + 1, y))[G])
        if dif != 42:
            print(chr(dif), end='')
print()
# he hidden message is whodunnit().split()[0] ?

def whodunnit():
    return 'Guido van Rossum'

print(whodunnit().split()[0])