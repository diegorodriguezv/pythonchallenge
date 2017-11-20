# LEVEL 20
# http://www.pythonchallenge.com/pc/hex/idiot2.htmlhttp://www.pythonchallenge.com/pc/hex/idiot2.html

import re

import requests

url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
req = requests.head(url, auth=('butter', 'fly'))
print(req.headers)
print(req.status_code)

while req.status_code != 416:
    h = req.headers['content-range']
    parts = re.findall('bytes (\d+)-(\d+)/(\d+)', h)[0]
    start = int(parts[0])
    end = int(parts[1])
    total = int(parts[2])
    print(start, end, total)
    headers = {'range': 'bytes={}-'.format(end + 1)}
    req = requests.get(url, auth=('butter', 'fly'), headers=headers)
    print(req.headers)
    print(req.status_code)
    print(req.content)

headers = {'range': 'bytes={}-'.format(total + 1)}
req = requests.get(url, auth=('butter', 'fly'), headers=headers)
print(req.headers)
print(req.status_code)
print(''.join(reversed(str(req.content))))
print(''.join(reversed('invader')))

h = req.headers['content-range']
parts = re.findall('bytes (\d+)-(\d+)/(\d+)', h)[0]
start = int(parts[0])
end = int(parts[1])
total = int(parts[2])
print(start, end, total)
headers = {'range': 'bytes={}-'.format(start - 1)}
req = requests.get(url, auth=('butter', 'fly'), headers=headers)
print(req.headers)
print(req.status_code)
print(req.content)
# b'and it is hiding at 1152983631.\n'


headers = {'range': 'bytes={}-'.format(1152983631)}
req = requests.get(url, auth=('butter', 'fly'), headers=headers)
print(req.headers)
print(req.status_code)
print(req.content)

with open('data/level_20.zip', 'wb') as f:
    f.write(req.content)
