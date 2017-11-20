# LEVEL 23
# www.pythonchallenge.com/pc/hex/bonus.html

import this

# ROT13
first = ord('a')
last = ord('z')
str1 = "".join([chr(x) for x in range(first, last + 1)])
str2 = "".join([chr(first + x + 13 - last - 1) if x + 13 > last else chr(x + 13) for x in range(first, last + 1)])
print(str1)
print(str2)
table = str.maketrans(str1, str2)
print('va gur snpr bs jung?'.translate(table))
# in the face of what?
