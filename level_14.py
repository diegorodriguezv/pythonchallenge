# LEVEL 14
# http://www.pythonchallenge.com/pc/return/italy.html

from PIL import Image, ImageDraw

wire_file = Image.open('data/wire.png')
wire = wire_file.load()
print(wire_file.mode)
w, h = wire_file.size
result_image = Image.new('RGBA', (100, 100), 'black')
result = ImageDraw.Draw(result_image)
wire_x = 0
for j in range(100):
    for i in range(100):
        result.point((i, j), wire[wire_x, 0])
        wire_x += 1
result_image.save('data/wire_square.png')
# the image reads "bit" but bit.html says: you took the wrong turn

result_image = Image.new('RGBA', (1000, 50), 'black')
result = ImageDraw.Draw(result_image)
y = 0
x = 0
for i in range(w):
    px = wire[i, 0]
    if px == (232, 41, 41):
        x = 0
        y += 1
    else:
        x += 1
    result.point((x, y), px)
result_image.save('data/wire_slice.png')

result_image = Image.new('RGBA', (100, 100), 'black')
result = ImageDraw.Draw(result_image)
wire_x = 0
side = 100
for border in range(0, side // 2):
    for x in range(border, side - border):
        result.point((x, border), wire[wire_x, 0])
        wire_x += 1
    for y in range(border + 1, side - border):
        result.point((x, y), wire[wire_x, 0])
        wire_x += 1
    for x in range(y - 1, border - 1, -1):
        result.point((x, y), wire[wire_x, 0])
        wire_x += 1
    for y in range(side - border - 2, border, -1):
        result.point((x, y), wire[wire_x, 0])
        wire_x += 1
print(wire_x)  # should be 100 * 100 = 10000
result_image.save('data/wire_roll.png')
