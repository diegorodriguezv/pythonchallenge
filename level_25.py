# LEVEL 25
# http://www.pythonchallenge.com/pc/hex/lake.html
import wave

from PIL import Image

# import requests
# i = 0
# while True:
#     i += 1
#     req = requests.get('http://www.pythonchallenge.com/pc/hex/lake{}.wav'.format(i), auth=('butter', 'fly'))
#     if req.status_code == 200:
#         with open('data/lake{}.wav'.format(i), 'wb') as f:
#             f.write(req.content)
#     else:
#         break

images = []
for i in range(1, 26):
    with wave.open('data/lake{}.wav'.format(i), 'rb') as f:
        print(f.getparams())
        data = f.readframes(f.getnframes())
    images.append(Image.frombytes('RGB', (60, 60), data))
print(len(images))
img = Image.new('RGB', (300, 300))
index = 0
for i in range(5):
    for j in range(5):
        img.paste(images[index], (j * 60, i * 60))
        index += 1
img.save('data/level_25.png')
