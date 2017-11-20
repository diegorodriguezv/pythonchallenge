# LEVEL 22
# http://www.pythonchallenge.com/pc/hex/copper.html

from PIL import Image

img = Image.open('data/white.gif')
movements = []
w, h = img.size
frame = 1
while True:
    try:
        print(img.histogram())
        pos_count = 0
        for i in range(w):
            for j in range(h):
                if img.getpixel((i, j)) == 8:
                    movements.append((i - 100, j - 100))
                    pos_count += 1
        print(img.tell(), pos_count)
        img.seek(img.tell() + 1)
    except EOFError:
        break
print(movements)
print(len(movements))

count = 0
img = None
for mov in movements:
    if mov == (0, 0):
        if img:
            img.save('data/level_22.{}.gif'.format(count))
            count += 1
        img = Image.new('1', (60, 60))
        pos = (30, 30)
    pos = tuple(map(sum, zip(pos, mov)))
    img.putpixel(pos, 1)
img.save('data/level_22.{}.gif'.format(count))
