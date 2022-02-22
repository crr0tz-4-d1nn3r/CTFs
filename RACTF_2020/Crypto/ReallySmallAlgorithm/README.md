# Really Small Algorithm
150 points

Connet to service running (provided IP and port).

Connect to the network service to get the flag.

## References and Tools
see Really Simple writeup and
https://docs.sympy.org/latest/modules/ntheory.html

## Flag
Didn't write this one down. Something about "size matters"

## Solution
This is about the same as the previous challenge. This time, we are provided n, the product of the primes, vs the primes themselves.Parsing the data, we can capture (e, n) and ct. The pair (e, n) consitiute the public key. The encrypted message will be our cipher text (ct). I'm using the module 'factorint' from sympy.ntheory to factor n into primes. Use the same code as above, with the following modification
```python
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
```

Turns out one of the primes they used was a small value - like 17 or something. Hence "Really Small".
