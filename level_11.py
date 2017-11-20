# LEVEL 11
# http://www.pythonchallenge.com/pc/return/5808.html

from PIL import Image, ImageDraw

orig = Image.open('data/cave.jpg')
pix = orig.load()
w, h = orig.size
each_size = w // 2, h // 2
new1 = Image.new('RGB', each_size, 'black')
draw1 = ImageDraw.Draw(new1)
new2 = Image.new('RGB', each_size, 'black')
draw2 = ImageDraw.Draw(new2)

odd = True
for x in range(w):
    for y in range(h):
        px = pix[x, y]
        new_coords = (x // 2, y // 2)
        if odd:
            draw1.point(new_coords, px)
        else:
            draw2.point(new_coords, px)
        odd = not odd

new1.save('data/cave1.jpg')
new2.save('data/cave2.jpg')
