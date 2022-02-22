#!/usr/bin/python3
# NahamCon CTF 
# Cryptography
# Homecooked 
# 100 pts
# I cannot get this to decrypt!
# Download code
# cipher text is being xor'ed with primes
# but only palindorm primes.
# https://oeis.org/A002385/b002385.txt
# to let it run on it's own will take a very long time
# store primes as a lookup table
# flag{pR1m3s_4re_co0ler_Wh3n_pal1nDr0miC}

# New decode function
import base64

cipher_b64 = b"MTAwLDExMSwxMDAsOTYsMTEyLDIxLDIwOSwxNjYsMjE2LDE0MCwzMzAsMzE4LDMyMSw3MDIyMSw3MDQxNCw3MDU0NCw3MTQxNCw3MTgxMCw3MjIxMSw3MjgyNyw3MzAwMCw3MzMxOSw3MzcyMiw3NDA4OCw3NDY0Myw3NTU0MiwxMDAyOTAzLDEwMDgwOTQsMTAyMjA4OSwxMDI4MTA0LDEwMzUzMzcsMTA0MzQ0OCwxMDU1NTg3LDEwNjI1NDEsMTA2NTcxNSwxMDc0NzQ5LDEwODI4NDQsMTA4NTY5NiwxMDkyOTY2LDEwOTQwMDA="
pprimes = [2, 3, 5, 7, 11, 101, 131, 151, 181, 191, 313, 353, 373,
 70207, 70507, 70607, 71317, 71917, 72227, 72727, 73037, 73237, 73637, 74047, 74747, 75557,
 1003001, 1008001, 1022201, 1028201, 1035301, 1043401, 1055501, 1062601, 1065601, 1074701, 
 1082801, 1085801, 1092901, 1093901, 1114111, 1117111, 1120211]

cipher = base64.b64decode(cipher_b64).decode().split(",")
count = 0
while(count < len(cipher)):
    print(chr(int(cipher[count]) ^ pprimes[count]), end='', flush=True)
    count += 1

print()