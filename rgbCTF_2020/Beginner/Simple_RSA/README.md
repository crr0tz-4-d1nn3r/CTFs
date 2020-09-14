README

# Simple RSA
50 points, solve #131, 1 hour, 50 minutes after release (2020-07-11 18:50:53)

Can you find a way to attack this RSA implementation?

~qpwoeirut#5057

simple_rsa.txt Size: 0.12 KBMD5: 890e58f8d143ee2e7f761779500b591f

simple_rsa.py Size: 0.39 KBMD5: 292f34897f99b5b4178cadca1a725b80

## Flag
```shell
rgbCTF{brut3_f0rc3}
```

## Solution
Download provided files.  The text file contains the usual stuff:
```shell
n = 5620911691885906751399467870749963159674169260381
e = 65537
c = 1415060907955076984980255543080831671725408472748
```

The python file provides a simple RSA encryption algorithm. Nice starter if you haven't done these before. I had some code from previous CTFs that I leveraged for this.

Main idea: Given n, find primes p and q such that n = p*q. I used the python module factorint from sympy.ntheory (https://docs.sympy.org/latest/modules/ntheory.html). Then find phi = (p-1)(q-1). Then d = inverseMod(e,phi). Reconstruct the plain text (as an integer value) by pt = pow(c,d,n).