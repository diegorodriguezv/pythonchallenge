# LEVEL 12
# http://www.pythonchallenge.com/pc/return/evil.html

import string

with open('data/evil2.gfx', 'rb') as f:
    first_bytes = f.read(100)

# The picture shows someone dealing cards. It seems like each byte should be "dealt" to a different player (file) but we
# need to identify how many players are there.
num_players = 10
for players in range(1, num_players + 1):
    print('players: ' + str(players))
    player_chars = [''] * players
    for i in range(len(first_bytes)):
        byte = first_bytes[i]
        # if not str(byte).isprintable():
        if chr(byte) not in string.digits + string.ascii_letters + string.punctuation + ' ':
            byte = ord('.')
        player_chars[i % players] += chr(byte)
    for p in range(players):
        print('{}:  {}'.format(p, player_chars[p]))

# 5 players show a certain symmetry, after inspecting https://en.wikipedia.org/wiki/List_of_file_signatures we find that
# the headers coincide with (JPEG, PNG, GIF, PNG, JPEG)

num_players = 5
streams = [bytes()] * num_players
i = 0
with open('data/evil2.gfx', 'rb') as f:
    while True:
        next_byte = f.read(1)
        if not next_byte:
            break
        streams[i % num_players] += next_byte
        i += 1

ext = ['jpeg', 'png', 'gif', 'png', 'jpeg']
for n in range(num_players):
    print(len(streams[n]))
    with open('data/evil2.{}.{}'.format(n, ext[n]), 'wb') as f:
        f.write(streams[n])
