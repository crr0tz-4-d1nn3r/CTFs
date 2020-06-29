"""
raCTF 2020
Crypto/Really Simple Algorithm
connect to server, it provides:
    p, q, e and ct
use RSA inverse to decrypt ct
flag: ractf{JustLikeInTheSimulations}
"""
import math

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
    p = 9809820989653234011777079707374936696750260082873443226211940951627565575560770831305320404158860313104843691251667686556207491587640420556392327293117927
    q = 12606411276169056075514946810312714713544820085435068329176455919621941265122688321947336617968675859007146707024665532944786231106454433224868079551473419
    e = 65537
    ct = 15856969234697250734092362948503429272109361352985954933986882479406548684717876572969541870302144788931193341796282988676512382656059744424139718330334499133659758393546403637856648195375955891185433120899940589453754243195276361716281026037347426614515123809086892816181975122198698167258382053119515575246
   
    # compute n
    n = p * q

    # Compute phi(n)
    phi = (p - 1) * (q - 1)

    # Compute modular inverse of e
    d = getModInverse(e, phi)

    # Decrypt ciphertext
    pt = pow(ct, d, n)
    
    # print flag
    h = hex(pt)
    flag = bytes.fromhex(h[2:]).decode()
    print(flag)