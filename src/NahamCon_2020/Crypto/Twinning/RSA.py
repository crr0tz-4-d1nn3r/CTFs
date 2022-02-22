#!/usr/bin/python3
# NahamCon CTF 
# Cryptography
# Twinning 
# 100 pts
# Text: These numbers wore the same shirt! LOL, #TWINNING!
# Connect to service
# It generates some cypher text with what looks like RSA
# provides the pair (e,n)
# To solve, make a guess at one of the prime values
# Hopefully, you find something with this guess.
# Create the other prime, and phi, then use reverse mod to get d (private key)
# decrypt the cipher text to get the PIN
# Submit the PIN to win :)
# flag{thats_the_twinning_pin_to_win}


import socket
import math
from time import sleep
import re
from sympy.ntheory import factorint

def getModInverse(a, m):
    if math.gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = 
            (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

    
if __name__ == "__main__":
    # connect to service
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('jh2i.com', 50013))
    # there is some lag on this challenge
    sleep(15)
    data = client.recv(5000) 
    print(data.decode())
    
    
    # parse the provided public key and cipher text
    D = data.decode().split('\n')
    r = re.search('(\d+),(\d+)', D[1])    
    e = int(r.group(1))
    n = int(r.group(2))    
    r = re.search('(\d+)', D[2])  
    ct = int(r.group(1))
    
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
        print(pt)
        
        # send decoded PIN and get flag
        client.send(str(pt).encode() + b'\n')
        sleep(1)
        print(client.recv(5000).decode())
        client.close()