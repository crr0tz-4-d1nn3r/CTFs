#!/usr/bin/python3
# NahamCon CTF 
# Cryptography
# Raspberry 
# 125 pts
# Raspberries are so tasty. I have to have more than just one!
# Downoad text file containing n, e, and c
# Appears to be another RSA challenge, but with much bigger numbers
# Factoring is handled by factorint from sympy
# Turns out this RSA is made with 32 primes.
# See multi-prime RSA
# https://bitsdeep.com/posts/attacking-rsa-for-fun-and-ctf-points-part-4/
# flag{there_are_a_few_extra_berries_in_this_one}

import math
from sympy.ntheory import factorint

def getModInverse(a, m):
    if math.gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

if __name__ == "__main__":
        
    e = 65537
    n = 7735208939848985079680614633581782274371148157293352904905313315409418467322726702848189532721490121708517697848255948254656192793679424796954743649810878292688507385952920229483776389922650388739975072587660866986603080986980359219525111589659191172937047869008331982383695605801970189336227832715706317
    ct = 5300731709583714451062905238531972160518525080858095184581839366680022995297863013911612079520115435945472004626222058696229239285358638047675780769773922795279074074633888720787195549544835291528116093909456225670152733191556650639553906195856979794273349598903501654956482056938935258794217285615471681

    d = factorint(n)
    pd = list(d.keys())
       
    if len(pd) == 0:
        print('Houston, we have a problem')
    else:
        phi = 1
        for p in pd:
            phi *= (p-1)
            
        d = getModInverse(e, phi)
        
        # Decrypt ciphertext
        pt = pow(ct, d, n)
        h = hex(pt)
        flag = bytes.fromhex(h[2:]).decode()
        print(flag)