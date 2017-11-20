# LEVEL 24 (second part)
import hashlib
import zipfile
from io import BytesIO

with zipfile.ZipFile('data/level_24.zip') as zf:
    for zi in zf.infolist():
        print(zi)
    zf_data_b = zf.read('mybroken.zip')
    zf_data = BytesIO(zf_data_b)
    with zipfile.ZipFile(zf_data) as bzf:
        for zi in bzf.infolist():
            print(zi)
md5_h = hashlib.md5()
md5_h.update(zf_data_b)
print(md5_h.hexdigest())


# certutil -hashfile mybroken.zip MD5
# bb f6 61 69 28 e2 3e cf ef 4b 71 7f 28 1c 53 cc
# leopold's email
# bbb8b499a0eef99b52c7f13f4e78c24b

# 7zip reports there are two errors but perhaps they are the crc for the compressed file and the crc for the whole
# archive so maybe there is only one corrupted byte. If so, let's try to generate a file with the correct MD5 checksum
# by changing one byte at a time
def try_to_fix(data, expected_md5):
    for i in range(len(data)):
        for val in range(256):
            fixed = data[:i] + bytes([val]) + data[i + 1:]
            md5_h = hashlib.md5()
            md5_h.update(fixed)
            if md5_h.hexdigest() == expected_md5:
                print('fixed!')
                return fixed
    return None


fixed = try_to_fix(zf_data_b, 'bbb8b499a0eef99b52c7f13f4e78c24b')
if fixed:
    with open('data/level_24b_fixed.zip', 'wb') as f:
        f.write(fixed)
    zf_data = BytesIO(fixed)
    with zipfile.ZipFile(zf_data) as bzf:
        for zi in bzf.infolist():
            print(zi)
        gif_data = bzf.read('mybroken.gif')
    with open('data/mybroken_fixed.gif', 'wb') as gf:
        gf.write(gif_data)
# it's a gif image with the word "speed" written in blue