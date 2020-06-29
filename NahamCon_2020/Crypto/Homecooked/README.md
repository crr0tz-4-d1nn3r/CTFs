README

# Homecooked
100 points

I cannot get this to decrypt!

Download the file below.

decrypt.py

## Flag
```shell
flag{pR1m3s_4re_co0ler_Wh3n_pal1nDr0miC}
```

## Solution
The provided python code include the cipher text (base 64 encoded) and a method for decrypting.
```python
cipher_b64 = b"MTAwLDExMSwxMDAsOTYsMTEyLDIxLDIwOSwxNjYsMjE2LDE0MCwzMzAsMzE4LDMyMSw3MDIyMSw3MDQxNCw3MDU0NCw3MTQxNCw3MTgxMCw3MjIxMSw3MjgyNyw3MzAwMCw3MzMxOSw3MzcyMiw3NDA4OCw3NDY0Myw3NTU0MiwxMDAyOTAzLDEwMDgwOTQsMTAyMjA4OSwxMDI4MTA0LDEwMzUzMzcsMTA0MzQ0OCwxMDU1NTg3LDEwNjI1NDEsMTA2NTcxNSwxMDc0NzQ5LDEwODI4NDQsMTA4NTY5NiwxMDkyOTY2LDEwOTQwMDA="
```

Decodeing the cipher text:
```python
cipher = base64.b64decode(cipher_b64).decode().split(",")
```

It's a  list of numbers:
```python
cipher = ['100', '111', '100', '96', '112', '21', '209', '166', '216', '140', '330', '318', '321', '70221', '70414', '70544', '71414', '71810', '72211', '72827', '73000', '73319', '73722', '74088', '74643', '75542', '1002903', '1008094', '1022089', '1028104', '1035337', '1043448', '1055587', '1062541', '1065715', '1074749', '1082844', '1085696', '1092966', '1094000']
```

Stepping through the method provided in the code reveals that they are decoding each value with increasing values of primes. However, not all primes - and after a while the program starts to lag. Looking at the primes that are being used before stopping execution:
```python
pprimes = [2, 3, 5, 7, 11, 101, 131, 151, 181, 191, 313, 353, 373]
```

Funny - palindomes. We could speed up execution by storing the list on primes. Good site for finding lists of number sequences: https://oeis.org/. Found the list we need for this problem at https://oeis.org/A002385/b002385.txt. With the primes stored (40 of them as that's the length of the cipher array), we use a simple while loop to decode and print the flag:
```python
pprimes = [2, 3, 5, 7, 11, 101, 131, 151, 181, 191, 313, 353, 373, 70207, 70507, 70607, 71317, 71917, 72227, 72727, 73037, 73237, 73637, 74047, 74747, 75557, 1003001, 1008001, 1022201, 1028201, 1035301, 1043401, 1055501, 1062601, 1065601, 1074701, 1082801, 1085801, 1092901, 1093901, 1114111, 1117111, 1120211]
count = 0
while(count < len(cipher)):
    print(chr(int(cipher[count]) ^ pprimes[count]), end='', flush=True)
    count += 1
```
The flag is printed as output.

