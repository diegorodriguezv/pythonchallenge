# LEVEL 4
# http://www.pythonchallenge.com/pc/def/linkedlist.php
# 12345
# 44827
# 45439
# 94485
# 72198
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
# and the next nothing is 44827

import re
import urllib.request

nothing = '12345'
finish = False
while not finish:
    response = urllib.request.urlopen(
        'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nothing).read().decode("utf-8")
    all = re.findall('nothing is (\d*)', response)
    if all:
        nothing = all[0]
        print(nothing)
    else:
        finish = True
        print(response)

nothing = str(int(int(nothing) / 2))
finish = False
while not finish:
    response = urllib.request.urlopen(
        'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nothing).read().decode("utf-8")
    all = re.findall('nothing is (\d*)', response)
    if all:
        nothing = all[0]
        print(nothing)
    else:
        finish = True
        print(response)
