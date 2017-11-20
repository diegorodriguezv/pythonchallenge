# LEVEL 21
# (zip from previous level)

import bz2
import zipfile
import zlib

with zipfile.ZipFile('data/level_20.zip') as myzip:
    for zi in myzip.infolist():
        print(zi)
        # print(zi.comment)
    with myzip.open('readme.txt', 'r', pwd=b'redavni') as zf:
        # print(myzip.getinfo('readme.txt'))
        for l in zf:
            print(l)
    with myzip.open('package.pack', 'r', pwd=b'redavni') as zf2:
        data = zf2.read()
known = [b'x\x9c', b'BZ']
stop = False
message = ''
accum = 0
while not stop:
    decompressed = 0
    while data[:2] == b'x\x9c':
        decompressed += 1
        data = zlib.decompress(data)
        message += ' '
    # print('zlib:', decompressed)
    accum += decompressed
    decompressed = 0
    while data[:3] == b'BZh':
        decompressed += 1
        data = bz2.decompress(data)
        message += '*'
    # print('bz2:', decompressed)
    accum += decompressed
    if data[:2] not in known:
        data = data[::-1]
        # print('inv', accum)
        message += '\n'
        accum = 0
        if data[:2] not in known:
            stop = True

print(len(data))
print(data[:20])
print(data[-20:])
print(message)
print(len(message))
