# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 15:07:43 2020
"""


b = bytearray(b'M>N\xe1\x90\x14/\xcf<I9\xdb\xc8\x04\x82\x86\xa6\xa7\xb4\xd7%\xffB\xbb\xe5\xfc6m\xdc\x11\xc5\xa1\xdfv\x8b\x17\xfa\xc7\xde\xf9')
n = 1719369980666357291413282150426450168296389813823538353197967759679

"""
reversing the following to get g
    g = b"rgbCTF{REDACTED}"
    b = bytearray([w(0, 255) for _ in range(40)])

    n = int.from_bytes(bytearray([l ^ p for l, p in zip(g, b)]), 'little')
    print("Here's another number I found: ", n)
"""

nb =  bytearray(n.to_bytes(40, 'little'))

for i in range(40):
    print(chr(nb[i] ^ b[i]), end='')
