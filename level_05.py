# LEVEL 5
# http://www.pythonchallenge.com/pc/def/peak.html

import pickle

test = {'a': 2, 'b': 4, 'c': 6,
        'alongstring0': 'averylongstringindeed0',
        'alongstring1': 'averylongstringindeed1',
        'alongstring2': 'averylongstringindeed2',
        'alongstring3': 'averylongstringindeed3',
        'alongstring4': 'averylongstringindeed4',
        'alongstring5': 'averylongstringindeed5',
        'alongstring6': 'averylongstringindeed6',
        'alongstring7': 'averylongstringindeed7',
        'alongstring8': 'averylongstringindeed8',
        }

test2 = {}

try:
    with open('data/level_5_test.p', 'wb') as f:
        data = pickle.dump(test, f, 0)  # found protocol 0 produces output similar to banner.p
        print(data)
    with open('data/level_5_test.p', 'rb') as f:
        data = pickle.load(f)
        print(data)
except Exception as exc:
    raise exc
    pass

histogram = {}
try:
    with open('data/banner.p', 'rb') as f:
        data = pickle.load(f)
except Exception as exc:
    raise exc
    pass

lists = [l for l in data]
for list in lists:
    total_times = 0
    for char, times in list:
        total_times += times
        print(char * times, end='')
    print()
