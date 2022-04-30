import random

ct = open('out', 'r').read()

# k = 39137
for k in range(0xfffd):
    pt = ''
    for c in ct:
        res = (ord(c) - k) % 0xFFFD
        pt += chr((ord(c) - k) % 0xFFFD)
    if 'flag' in pt:
        print(f'{k}: {pt}')
        break

