# LEVEL 2
# http://www.pythonchallenge.com/pc/def/ocr.html
# find rare characters in the mess below:

histogram = {}
try:
    with open('data\level_2.data') as f:
        for line in f:
            for char in line:
                if char in histogram:
                    histogram[char] += 1
                else:
                    histogram[char] = 1
except Exception as exc:
    print(str(exc)[:50])
rare = set()
for k, v in histogram.items():
    if v < 100:
        rare.update(k)
print(rare)
secret = ""
try:
    with open('data\level_2.data') as f:
        for line in f:
            for char in line:
                if char in rare:
                    secret += char
except Exception as exc:
    print(str(exc)[:50])
print(secret)
