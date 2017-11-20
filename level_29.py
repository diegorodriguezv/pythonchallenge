# LEVEL 29
# http://www.pythonchallenge.com/pc/ring/guido.html
# There are several blank lines at the end of the page
import requests

req = requests.get('http://www.pythonchallenge.com/pc/ring/guido.html', auth=('repeat', 'switch',))
content = req.content
doc, spaces = content.split(b'</html>\n')
print(len(spaces))
print(len(doc))
print(len(content))
print(spaces)
print(doc)
print(content)
message = bytearray()
lines = spaces.split(b'\n')
for l in lines:
    print(len(l))
    message.append(len(l))

import bz2
print(bz2.decompress(message))
# Isn't it clear? I am yankeedoodle!
