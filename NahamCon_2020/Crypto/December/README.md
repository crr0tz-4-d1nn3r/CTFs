README

# December
125 points

This is my December...

Download the file below.

source.py, ciphertext

## Flag 
```shell
flag{this_is_all_i_need}
```

## Solution
We are provided a bit of source code and some cipher text. It looks like a simple DES encryption. We are even provided the initiation vector (iv). We are not given the key. But, maybe the title and flavor text can help? To google! Two main hits: Linkin Park and Kelly Clarkson. Key's I tried, using CyberChef (https://gchq.github.io/CyberChef):

december, December, d3c3mb3r, D3c3mb3R, d3cymb3r, d3cimb3r, d3c1mb3r, MyDe>mbr

as well as multiple versions of both artists names ...

Wikipedia list a couple weak keys (https://en.wikipedia.org/wiki/Weak_key), maybe those? Yep, 0x1F1F1F1F0E0E0E0E works perfectly:
```shell
These are my snow covered dreams
This is me pretending
flag{this_is_all_i_need}.
```

https://www.azlyrics.com/lyrics/linkinpark/mydecember.html

So glad that worked. Brute force would take a while.