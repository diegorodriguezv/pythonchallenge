# LEVEL 18
# http://www.pythonchallenge.com/pc/return/balloons.html

import difflib
import gzip

with gzip.open('data/deltas.gz', 'rt') as f:
    left = []
    right = []
    while True:
        line = f.readline()
        if line:
            # print(line)
            left.append(line[:53])
            right.append(line[56:].rstrip(' \n'))
        else:
            break
print(len(left))
print('-' + left[0] + '-')
print(len(right))
print('-' + right[0] + '-')

differ = difflib.ndiff(left, right)
left, right, center = [], [], []
for line in differ:
    if line[0] == '+':
        left.append(line[2:])
    elif line[0] == '-':
        center.append(line[2:])
    elif line[0] == ' ':
        right.append(line[2:])
    else:
        print('Line not present in either sequence.')

print(len(left))
print('-' + left[0] + '-')
print(len(right))
print('-' + right[0] + '-')
print(len(right))
print('-' + center[0] + '-')
file_names = ['data/deltas.{}.png'.format(i) for i in (1, 2, 3)]
contents = [left, right, center]
for fn, con in zip(file_names, contents):
    with open(fn, 'wb') as f:
        for line in con:
            f.write(bytearray.fromhex(line))
