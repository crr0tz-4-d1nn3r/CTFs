README

# Occasionally Tested Protocol
219 points, solve #42, 3 hours, 54 minutes after release (2020-07-11 20:54:19)

But clearly not tested enough... can you get the flag?

nc 167.172.123.213 12345

otp.py

## Flag
```shell
rgbCTF{random_is_not_secure}
```

## Solution
Connecting to the service we get 11 numbers
```shell
54 6129 4944 1271 9543 9158 5685 5405 4230 6182
2371765254082916291151617788837842918940177317831489985988827882731
```

Looking at the provided python code, it uses time to seed the PRNG. It prints 10 numbers and then xor's the flag with an array of 40 additional random values (same seed).  If we can time it correctly (i.e. generate the same seed), we can probably reverse this. Running the code on my machine and on the server, after a few tries, success, 10 matching numbers.

Taking the array of 40 numbers used in the "encryption" and xor-ing with teh 11th value provided by the serverr produces the flag.