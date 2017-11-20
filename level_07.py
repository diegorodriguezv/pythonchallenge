# LEVEL 7
# http://www.pythonchallenge.com/pc/def/oxygen.html
# png code in grayscale

from PIL import Image

im = Image.open("data/oxygen.png")
pix = im.load()
w, h = im.size
for y in range(h):
    repeated_pixels = 0
    for x in range(w - 1):
        repeated_pixels += 1
        left_pixel = pix[x, y]
        right_pixel = pix[x + 1, y]
        if left_pixel != right_pixel:
            break
    if repeated_pixels > 3:
        index = 0
        seq_sizes = [0]
        for x in range(w - 1):
            seq_sizes[index] += 1
            left_pixel = pix[x, y]
            right_pixel = pix[x + 1, y]
            if left_pixel != right_pixel:
                if seq_sizes[index] < 3:
                    del seq_sizes[index]
                    break
                seq_sizes.append(0)
                index += 1
        message_width = sum(seq_sizes)
        pixels = []
        message = ''
        x = 0
        while x < message_width:
            pixels.append(pix[x, y])
            message += chr(pix[x, y][0])
            x += 7
        print(message)
        break

next_codes = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join([chr(code) for code in next_codes]))
