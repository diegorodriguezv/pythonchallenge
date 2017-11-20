# LEVEL 6
# http://www.pythonchallenge.com/pc/def/channel.html
# http://www.pythonchallenge.com/pc/def/channel.zip

from zipfile import ZipFile
import re

with ZipFile('data\channel.zip', 'r') as myzip:
    # for zi in myzip.infolist():
    #     # print(zi)
    #     print(zi.comment)
    # with myzip.open('readme.txt', 'r') as zf:
    #     print(myzip.getinfo('readme.txt'))
    #     for l in zf:
    #         print(l)

    nothing = '90052'
    finish = False
    comments = ''
    while not finish:
        fn = nothing + '.txt'
        zi = myzip.getinfo(fn)
        # print(zi.comment.decode())
        comments += zi.comment.decode()
        with myzip.open(zi, 'r') as zf:
            for l in zf:
                all = re.findall('nothing is ([0-9]*)', str(l))
                if len(all) == 1:
                    nothing = all[0]
                else:
                    print(l.decode())
                    finish = True
    print(comments)
