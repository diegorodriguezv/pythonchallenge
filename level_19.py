# LEVEL 19
# http://www.pythonchallenge.com/pc/hex/bin.html

import base64


with open('data/level_19.txt', 'rb') as f:
    content = f.read()
    decoded = base64.decodebytes(content)
    with open('data/indian_little.wav', 'wb') as wav_l:
        with open('data/indian_big.wav', 'wb') as wav_b:
            data_start = 45
            # write header as is
            wav_l.write(decoded[:45])
            wav_b.write(decoded[:45])
            # change endianness for the rest of 16 bit words
            while True:
                if data_start + 2 <= len(decoded):
                    word_b = decoded[data_start:data_start + 2]
                    word_i_b = int.from_bytes(word_b, 'big')
                    word_l = word_i_b.to_bytes(2, 'little')
                    wav_l.write(word_l)
                    wav_b.write(word_b)
                else:
                    break
                data_start += 2
