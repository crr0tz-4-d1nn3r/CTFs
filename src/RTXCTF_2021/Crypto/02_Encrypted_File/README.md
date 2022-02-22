#  Encrypted File
200

We found this file on the local network of the attackers after you cracked their wireless network but we can't seem to figure out what it is, it had a .zip extension but doesn't have the zip header present... maybe it's encoded in some way? Can you get into it?

We over heard two of the people talking while walking out of their building mentioning something about it being a good thing that they use a simple cipher to encode all their files... we don't know how it's relevant but there was also a note attached to a USB drive we found that said "Cipher Key: 0xDE".

[enc.zip.enc](enc.zip.enc)

# Flag
```
RTXFLAG{th4t_w4s_e4sy}
```

# Solution
The hints "simple cipher to encode all their files" and "0xDE" made me think XOR. Wrote a python script to XOR the file with 0xDE.
```python
enc_file = 'enc.zip.enc'
out_png = 'enc.zip'

with open(enc_file,'rb') as infh:
    with open(out_png,'wb') as outfh:
        byte = infh.read(1)
        while byte != b'':
            xor = int.from_bytes(byte,'big') ^ 0xDE
            outfh.write(bytes([xor]))
            byte = infh.read(1)
```

Now have a password protected zip archive.
[enc.zip](enc.zip)

Used fcrackzip and the rockyou password list.
```
$ fcrackzip -u -D -p rockyou.txt enc.zip
PASSWORD FOUND!!!!: pw == lovely
```

Unzip the archive and get the flag.

# References
- [http://oldhome.schmorp.de/marc/fcrackzip.html](http://oldhome.schmorp.de/marc/fcrackzip.html) Available from apt: ```sudo apt install fcrackzip```