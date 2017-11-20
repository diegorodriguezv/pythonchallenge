# level 27
# http://www.pythonchallenge.com/pc/hex/speedboat.html

from PIL import Image

img = Image.open('data/zigzag.gif')

print(img.mode)
print(img.size)
pix = list(img.getdata())
pal = img.getpalette()[::3]
his = img.histogram()
print('pix', len(pix), pix[:20])
# print('pal', len(pal), pal)
# print('his', len(his), his)


def translate(seq, table):
    """Translate a sequence with the values in table."""
    result = []
    for i in range(len(seq)):
        result.append(table[seq[i]])
    return result


tra = translate(pix, pal)
print('tra', len(tra), tra[:20])
print(pix[1:110] == tra[:109])
print(pix[1:120] == tra[:119])


# the translated sequence looks a lot like the original shifted by one element but has some differences, let's find out

def compare(seq1, seq2):
    assert len(seq1) == len(seq2)
    same, diff = [], []
    diff1 = bytearray()
    diff2 = bytearray()
    img = []
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            same.append(seq1[i])
            img.append(1)
        else:
            diff.append((i, seq1[i], seq2[i]))
            diff1.append(seq1[i])
            diff2.append(seq2[i])
            img.append(0)
    return same, diff, diff1, diff2, img


s, d, d1, d2, i = compare(pix[1:], tra[:-1])
print(len(d), d[:20])
print(s[:20])
print(d1[:20])
print(d2[:20])
new = Image.new('1', img.size)
new.putdata(i)
new.save('data/level_27.png')
# the image says "not keyword" "busy?"
import bz2

data = str(bz2.decompress(d1), 'ascii')
# data = str(bz2.decompress(d1))
# print(data.replace('..', '\n..'))
print()
import keyword
words = set(data.split(' '))
for word in words:
    if not keyword.iskeyword(word):
        print(word)

# http://www.pythonchallenge.com/pc/ring/bell.html
# u: repeat
# p: switch
