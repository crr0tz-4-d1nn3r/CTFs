# Twinning
100 points

These numbers wore the same short! LOL, #TWINNING!

Connect with:
...


## Flag 
```shell
flag{thats_the_twinning_pin_to_win}
```

## Solution
Connect to service:
```shell
Generating public and private key...
Public Key in the format (e,n) is: (65537,260179566083)
The Encrypted PIN is 197392885182
What is the PIN?
```

The values change each time we connect to the service. 

Parsing the data, we can capture (e, n) and ct. The pair (e, n) consitiute the public key. The encrypted PIN will be our cipher text (ct). I'm using the module 'factorint' from sympy.ntheory (https://docs.sympy.org/latest/modules/ntheory.html) to factor n into primes. Then using Euler's Phi function to compute phi that when used with e can find the multiplicative inverse (d) modulo phi (https://en.wikipedia.org/wiki/Modular_multiplicative_inverse). Finding d is an iterative method based on Chineese Remainder Theorem.
```python
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
```

With d computed, we can decrypt the cipher text. The decoded message is an integer that, in most applications needs further processing. In this challenge, our responce to the service is the integer we compute. Sending that, we recieve our flag:
```shell
9232
Good job you won!
flag{thats_the_twinning_pin_to_win}
```

If your wondering, like I was, why the name of the challenge was "Twinning", take a look at the primes used in generating n:
```python
[510077, 510079]
```

Primes that differ by 2 are called twin primes. Cute.


