# LEVEL 16
# http://www.pythonchallenge.com/pc/return/mozart.html

from PIL import Image, ImageDraw

orig_img = Image.open('data/mozart.gif')
orig_pix = orig_img.load()
w, h = orig_img.size
print(orig_img.size)
purple = 195  # found after looking for repeated pixels
markers = []
for y in range(h):
    x = 0
    while x < w:
        prev = orig_pix[x, y]
        run = 1
        # look for runs of repeated pixels
        for offset in range(1, 10):
            if x + offset < w:
                pix = orig_pix[x + offset, y]
                if pix == prev:
                    run += 1
                else:
                    break
        if run > 4 and prev == purple:
            print('{:3},{:3}: {:2} | '.format(x, y, run), end='')
            print(orig_pix[x - 1, y], end=' ')
            for i in range(run):
                print(orig_pix[x + i, y], end=' ')
            print(orig_pix[x + run, y], end=' ')
            print()
            markers.append(x)
        x += run
res_img = Image.new(orig_img.mode, orig_img.size)
res_img.palette = orig_img.palette
res_drw = ImageDraw.Draw(res_img)
for y in range(h):
    for x in range(w):
        res_drw.point((x, y), orig_pix[(x + markers[y]) % w, y])
res_img.save('data/level_16.gif')
