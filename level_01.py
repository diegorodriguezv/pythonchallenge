# LEVEL 1
# http://www.pythonchallenge.com/pc/def/map.html

scrambled = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
new = ""
first = ord('a')
last = ord('z')
print(scrambled)
for c in scrambled:
    if c not in ".' ()":
        num = ord(c) + 2
        if num > last:
            num = first + num - last - 1
        new += chr(num)
    else:
        new += c
print(new)
str1 = "".join([chr(x) for x in range(first, last + 1)])
str2 = "".join([chr(first + x + 2 - last - 1) if x + 2 > last else chr(x + 2) for x in range(first, last + 1)])
print(str1)
print(str2)
table = str.maketrans(str1, str2)
print(scrambled.translate(table))
print("http://www.pythonchallenge.com/pc/def/map.html".translate(table))

