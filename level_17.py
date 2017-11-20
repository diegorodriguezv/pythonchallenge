# LEVEL 17
# http://www.pythonchallenge.com/pc/return/romance.html

# import requests
#
# url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
# r = requests.get(url, auth=('huge', 'file'))
# print(r.cookies)
# print(len(r.cookies))
# print(r.headers)
# print(r.text)
# 'Set-Cookie': 'info=you+should+have+followed+busynothing...;

# import urllib.request
#
# password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
# top_level_url = "http://www.pythonchallenge.com/pc/return/"
# password_mgr.add_password(None, top_level_url, 'huge', 'file')
# handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
# cookieProcessor = urllib.request.HTTPCookieProcessor()
# opener = urllib.request.build_opener(cookieProcessor, handler)
# urllib.request.install_opener(opener)
# try:
#     response = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php')
#     print(response.read().decode('utf-8'))
#     print(response.geturl())
#     print(response.info())
#     print(response.getheader('Set-Cookie'))
#     print(response.headers.get('Set-Cookie'))
# except urllib.error.HTTPError as exc:
#     print(exc)
#     print(exc.read().decode('8859'))

# import re
# import urllib.request
# import bz2
# password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
# cookieProcessor = urllib.request.HTTPCookieProcessor()
# opener = urllib.request.build_opener(cookieProcessor)
# urllib.request.install_opener(opener)
# nothing = '12345'
# finish = False
# req_no = 0
# message = b''
# while not finish:
#     response = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=' + nothing)
#     req_no += 1
#     cookie = response.getheader('Set-Cookie')
#     all = re.findall('info=([^;]+);', cookie)
#     if all:
#         byte_str = all[0]
#         if '%' in byte_str:
#             message += bytearray.fromhex(byte_str[1:])
#         else:
#             if byte_str == '+':
#                 message += bytes(' ', 'utf-8')
#             else:
#                 message += bytes(byte_str, 'utf-8')
#     print(req_no, cookie)
#     text = response.read().decode("utf-8")
#     all = re.findall('busynothing is (\d*)', text)
#     if all:
#         nothing = all[0]
#         print(nothing)
#     else:
#         finish = True
#         print(text)
# print(message)
# print(bz2.decompress(message))
# b'is it the 26th already? call his father and inform him that "the flowers are on their way". he\'ll understand.'


import xmlrpc.client

with xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") as proxy:
    print(proxy.system.listMethods())
    phone = proxy.phone('Leopold')
    print(phone)
# 555-VIOLIN

import urllib.request
url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
req = urllib.request.Request(url)
req.add_header('Cookie', 'info=the flowers are on their way')
response = urllib.request.urlopen(req)
text = response.read().decode('utf-8')
print(text)
