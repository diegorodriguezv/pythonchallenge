# LEVEL 3
# http://www.pythonchallenge.com/pc/def/equality.html
# One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

import re

try:
    with open('data/level_3.data') as f:
        line_no = 0
        for line in f:
            line_no += 1
            all = re.findall('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]', line)
            if all:
                # print(''.join([each[4] for each in all]), end='')
                print(''.join([each[4] for each in all]), end='')

        print()
except Exception as exc:
    print(str(exc)[:50])
