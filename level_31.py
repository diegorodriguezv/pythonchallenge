# LEVEL 31
# http://www.pythonchallenge.com/pc/ring/grandpa.html
# where am I?
# a google goggles search tells me this is Koh Samui, Thailand
# http://www.pythonchallenge.com/pc/rock/grandpa.html
# u: kohsamui
# p: thailand
# That was too easy. You are still on 31...
# 	<img src="mandelbrot.gif" border="0">
# 		<window left="0.34" top="0.57" width="0.036" height="0.027"/>
# 		<option iterations="128"/>
# 	</img>

from collections import Counter

from PIL import Image


def scale(num, num_start, num_end, scale_start, scale_end):
    """Convert a number in one scale (num_start, num_end) to another scale (scale_start, scale_end)."""
    orig_s = (num - num_start) / (num_end - num_start)
    new_s = orig_s * (scale_end - scale_start) + scale_start
    return new_s

left = 0.34
top = 0.57
width = 0.036
height = 0.027
iterations = 128

SAME, COLOR1, COLOR2 = 0, 1, 2
img = Image.open('data/mandelbrot.gif')
img.show('original')
img_w, img_h = img.size
diff_img = Image.new(img.mode, img.size)
new_img = Image.new(img.mode, img.size)
for y in range(img_h):
    for x in range(img_w):
        x0 = scale(x, 0, img_w, left, left + width)
        y0 = scale(y, 0, img_h, top, top + height)
        c = complex(x0, y0)
        z = complex(0, 0)
        iteration = 0
        while abs(z) < 2 and iteration < iterations:
            z = z ** 2 + c
            iteration += 1
        iteration -= 1
        inv_y = img_h - y - 1
        new_img.putpixel((x, inv_y), iteration)
        diff = iteration - img.getpixel((x, inv_y))
        diff_img.putpixel((x, inv_y), COLOR1 if diff < 0 else COLOR2 if diff > 0 else SAME)

new_img.putpalette(img.getpalette())
new_img.show('my mandelbrot')

pal = [0] * 256 * 3  # 256 colors with 3 bands, set to black
pal[COLOR1 * 3 + 0] = 255  # red band(0) for color 1
pal[COLOR2 * 3 + 2] = 255  # blue band(2) for color 2
diff_img.putpalette(pal)
diff_img.show('differences')
# 1679 = 23 * 73

diffs = [1 if pixel == COLOR2 else 0 for pixel in diff_img.getdata() if pixel != SAME]
print(len(diffs))
print(Counter(diffs))

result_img = Image.new('1', (73, 23))
result_img.putdata(diffs)
result_img.show()

result_img = Image.new('1', (23, 73))
result_img.putdata(diffs)
result_img.show()

neg = [not d for d in diffs]
result_img = Image.new('1', (73, 23))
result_img.putdata(neg)
result_img.show()

result_img = Image.new('1', (23, 73))
result_img.putdata(neg)
result_img.show()
