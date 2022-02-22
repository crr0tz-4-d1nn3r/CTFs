#  Layers
300

We found this file in a folder called "Layers" on an open FTP that was located within the network you cracked previously, we were able to connect to the FTP after you got the password out of that previous archive, we're not sure what the deal is but there was a readme.txt next to it that just said the passphrase is "onionshavelayers".

The name of the file is just "encrypted_file".

[encrypted_file](encrypted_file)

# Flag
```
RTXFLAG{th4t_suck3d_l4y3rs}
```

# Solution
The file is a base64 encoded string. Doing a quick decode showed the string "Salted" at the start. 

```
$ cat encrypted_file 
U2FsdGVkX18mkpj/R4a6Pjx4Lp+PA+CR/KCJG7XJfD5Q+QKEbiD21CIA5Yzaazc3
Ygnh7e/QNEOT5B6Jn2wLT79VzH7oP5uxB+Aezb+4s7EfzJPkANhmcSwGQbvkSP1N
LiFJexZsjoI7xiGYEKA0FKdbYsHaaah2742QqLqJw86TUaWoG4MP2Vj9yrkhSL7Y
sHXxNAQeq6HuCFxvkDzusYDmQw5OC1uHuzry21RZvoU2JqUXEqSzXXF5qVshw1O1
FljPl18ppCt2nGdQs2ocNeOOlw+m7BFXvsUq28yctH7uhgbjCJf7k0a/BHP0Gn7y
0at/MEqx4W3tRc+bmzAcYTacQZ+gieSLnYpOYcyQWEPfgurivHiC3KBd9NaWL0eG
PZy19+7x6ZJ/ytTX04SfQjbxbd7bXV2S9Shc8pUOCB1M2nnI54PNwqlCCzY3xIg1
5+YGGhte4DXtnr9zmgnimdbAruvnmQjYTx7JSJURZ2lz87j9Sauqvu5mxmjb8yGr
0a0tSJmLC90bqHiwsyqDsQ==
$ base64 -d encrypted_file 
Salted ...
```

What does file think this is?

```
$ file encrypted_file 
encrypted_file: openssl enc'd data with salted password, base64 encoded
```

Ah. Well. We have the password, but not the algorithm used. So - hunting around, found that aes128 seems to work.
```
openssl enc -aes128 -d -a -salt -k onionshavelayers -in encrypted_file -out enc.1 
```
[enc.1](enc.1)

The output is a base64 encoded string.
```
$ cat enc.1
U2FsdGVkX1/zJ47hlSkrIE5V06xXcj9SeGFz/jo1GsMr5oT902Ui0twM2lJOqEfe
2EPhdEupxHR3QTZJlGyrsSwmwCUQFZmVSP6n+/xaPy43WFGOh3ueb3VyKIsBPpKD
fz253Rwecc/6yer/s4WNzEXdcj/7pd4gDxdg7xp8c7iOyACroBPs7JiTUYbiD5QA
bHscyxiyPQfOKBktfrTul2IgmG8ZAoxLusfx7qgv2HYGUuGI2YFsCqgSpG9YnDfE
uyUmZYr2tuk89VONAAbxXcXHOb0M/NyIeZ1dt6stonjWaW3Qlq7m3QuTQJ0XAHnW
MyxkHDNYdTCrbNnT6zQMO+UvYHtTF862Iw8wUYV7guyzROQNfKfVww==
$ base64 -d enc.1
Salted ...
```

Checking file shows it's also ssl encoded.

```
$ file enc.1
enc.1: openssl enc'd data with salted password, base64 encoded
```

Is is aes128 again? No. Figuring this may go on for a while, and not sure which algo to use, I wrote a bash script to just try them all. First dump the cipher list to a text file and clean it up.

[ciphers.txt](ciphers.txt)

```
#!/bin/bash
for cipher in $(cat ciphers.txt); do
        cipher=${cipher%$'\n'}
        openssl enc $cipher -d -a -salt -in encrypted_file -k onionshavelayers -out enc.1 2>/dev/null
        if base64 -d enc.1 | grep -q "Salted"; then
            echo $cipher
            cat enc.1
            break
        fi    
done
```

That worked. However, it didn't work on the second round. None of the outputs are base64 encoded. So - what are they?

```
#!/bin/bash
for cipher in $(cat ciphers.txt); do
        cipher=${cipher%$'\n'}
        openssl enc $cipher -d -a -salt -in enc.1 -k onionshavelayers -out enc.2 2>/dev/null
        output=$(file enc.2)
        echo $cipher $output
done
```

This produced a lot of output, of course. Scanning through, there were a couple that were interesting:

```
-aes-256-ecb enc.2: ARJ archive data, v234, multi-volume, slash-switched, original name: \224T\376d\364\330H\001ih\243\213\233l\004\025\2054\302\352]\245, 60]
-bf enc.2: Zip archive data, at least v1.0 to extract
-bf-cbc enc.2: Zip archive data, at least v1.0 to extract
-blowfish enc.2: Zip archive data, at least v1.0 to extract
-camellia-128-cbc enc.2: DOS executable (COM, 0x8C-variant)
-camellia128 enc.2: DOS executable (COM, 0x8C-variant)
```

The rest was just data or empty. Not that those couldn't be the answers - but from running this with full output - the rest are just noise.

aes-256 is out - file size is off. Next on the list is blowfish.

```
openssl enc -blowfish -d -a -salt -k onionshavelayers -in enc.1 -out enc2.zip  
```

Archive is password protected - and no the one we have been using. Using fcrackzip and rockyou.txt
```
$ fcrackzip -u -D -p rockyou.txt enc2.zip

PASSWORD FOUND!!!!: pw == monkey
```

Use the password to extract the flag.