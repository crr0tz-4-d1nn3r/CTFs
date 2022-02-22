#!/usr/bin/python3
# NahamCon CTF 
# Cryptography
# Unvreakable Vase 
# 125 pts

# 

import base64
from math import log, ceil



# Providing the alphabets because I'm nice.
base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
base32_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
# basexxx…

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)


def extract_data_from_message(message, base_charset=base64_alphabet, pad='=', L=8):

    # Number of bits used to represent each value using the chosen charset.
    nb_bits = int(ceil(log(len(base_charset), 2)))

    # Length of a properly padded encoded string in bits.
    word_len = lcm(nb_bits, L)

    # Number of characters needed for a properly encoded string.
    nb_chars = word_len // nb_bits

    # Will contain the resulting binary string
    result = ''

    # Number of unused bits depending on the number of padding characters.
    ub_pad = {n: (word_len - n * nb_bits) % L for n in range(nb_chars)}


    if len(message) % (nb_chars) != 0:
        print('Padding error: ' + string)
        print('Skipping...')
        continue

    # Length of the padding in bytes.
    padding = message.count(pad)



    


if __name__ == "__main__":

    cipher = 'zmxhz3tkb2vzx3roaxnfzxzlbl9jb3vudf9hc19jcnlwdg9vb30='
    text = extract_data_from_message(cipher)
    print(text)

