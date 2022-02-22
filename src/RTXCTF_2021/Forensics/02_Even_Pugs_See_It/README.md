#  Even Pugs See It
200

After you decoded the previous image we found their bot accessing another one while logging it's traffic, this one seems to only contain the picture of a pug and was named "Even-Pugs-See-It" we're not sure what to make of this; can you figure it out?

[RTX-Stego-lvl2.zip](RTX-Stego-lvl2.zip)

# Flag
```
RTXFLAG{PUGGSY}
```

# Solution
Checked out the metatdata with exiftool. Nothing particularly flaggy.

Opened the image in stegsolve. Started looking at the various color planes. Found Red 0 had a message.
![solved.bmp](solved.bmp)

# Reference
- [https://github.com/zardus/ctf-tools/blob/master/stegsolve/install](https://github.com/zardus/ctf-tools/blob/master/stegsolve/install)