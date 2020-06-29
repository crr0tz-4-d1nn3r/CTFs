#!/usr/bin/python3
# NahamCon CTF 
# Cryptography
# Ooo-la-la 
# 100 pts
# Text: Uwu, wow! Those numbers are fine!
# Downoad text file containing N, e, and c
# Appears to be another RSA challenge, but with much bigger numbers
# flag{ooo_la_la_those_are_sexy_primes}

import math
from time import sleep
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
    n = 3349683240683303752040100187123245076775802838668125325785318315004398778586538866210198083573169673444543518654385038484177110828274648967185831623610409867689938609495858551308025785883804091
    ct = 87760575554266991015431110922576261532159376718765701749513766666239189012106797683148334771446801021047078003121816710825033894805743112580942399985961509685534309879621205633997976721084983
    
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
        pt = pow(ct, d, n)
        h = hex(pt)
        flag = bytes.fromhex(h[2:]).decode()
        print(flag)