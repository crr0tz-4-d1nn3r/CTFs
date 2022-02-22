# Really Simple Algorithm
100 points

Connet to service running (provided IP and port).

We found a strange service running over TCP (my my, there do seem to be a lot of those as of late!). Connect to the service and see if you can't exploit it somehow.

## References and Tools
http://www.math.toronto.edu/mathnet/soar/Spring/PDF/RSA.pdf

https://en.wikipedia.org/wiki/Modular_multiplicative_inverse

https://inventwithpython.com/cryptomath.py

## Flag
```shell
flag: ractf{JustLikeInTheSimulations}
```

## Solution
Really simple. It's RSA at it's easiest. Challenge provided the two primes used to create the cipher text. Thus no need to factor some large product of primes. What we are missing is the private key, whcih we can use Chineese Remainder Theorem to solve. From there we can decode the plain text message.


Connect to the service to get your p, q, and e values and the cipher text. USe the algo above to find d. Decrypt, decode, profit. Each connection to the service provides different values. These are provided by example.
```python
p = 9809820989653234011777079707374936696750260082873443226211940951627565575560770831305320404158860313104843691251667686556207491587640420556392327293117927
q = 12606411276169056075514946810312714713544820085435068329176455919621941265122688321947336617968675859007146707024665532944786231106454433224868079551473419
e = 65537
ct = 15856969234697250734092362948503429272109361352985954933986882479406548684717876572969541870302144788931193341796282988676512382656059744424139718330334499133659758393546403637856648195375955891185433120899940589453754243195276361716281026037347426614515123809086892816181975122198698167258382053119515575246
```


Compute n, phi and d:
```python   
# compute n
n = p * q

# Compute phi(n)
phi = (p - 1) * (q - 1)

# Compute modular inverse of e
d = getModInverse(e, phi)
```


This is the function I use to find d, the Multiplicative Modular Inverse, the key to decryption.
```python
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
```

Finish decrypting and get flag:
```python
# Decrypt ciphertext
pt = pow(ct, d, n)

# print flag
h = hex(pt)
flag = bytes.fromhex(h[2:]).decode()
print(flag)
```