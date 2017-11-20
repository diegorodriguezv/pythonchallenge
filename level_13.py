# LEVEL 13
# http://www.pythonchallenge.com/pc/return/disproportional.html

import xmlrpc.client

with xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") as proxy:
    print(proxy.system.listMethods())
    phone = proxy.phone('Bert')
    print(phone)
