# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 13:45:49 2020
rgbCTF{brut3_f0rc3}
"""

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
    n = 5620911691885906751399467870749963159674169260381
    e = 65537
    c = 1415060907955076984980255543080831671725408472748
    
    # find some prime factors
    factors = factorint(n)
    primes = list(factors.keys())
    
    if len(primes) < 2:
        print('Houston, we have a problem.')
    else:
        # create the private key
        phi = 1
        for p in primes:
            phi *= (p-1)
        d = getModInverse(e, phi)
        
        # Decrypt ciphertext
        pt = pow(c, d, n)
        # print flag
        h = hex(pt)
        flag = bytes.fromhex(h[2:]).decode()
        print(flag[::-1])