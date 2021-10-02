#  Archive Matryoshka
300

After using the data that you found in the previous image we ran into this archive inside of a folder called "Archive Matryoshka" the bot seems to rely on it to update itself, but we haven't figured out how to extract it; hopefully you can get it.

HINT: Not figuring out that piece? Google better... add more words to the query.

HINT2: Yes you need that tool, no the linux version won't work; not it's not already present in your Kali Linux Distro.

[flag](flag)

# Flag
```
RTXFLAG{COMPRESSION_SUCKS}
```

# Solution
Not quite a zip bomb. Peeled back a bucnh of layers. At some point I didn't even try to export any of the intermediary archives. 

At one point there was a WIM archive. Needed to install a library to handle that.

Finally got down to an archive with the magic number "KGB". Found a tool for linux to handle the compression. But as the hint suggested - it did not work.

So - spin up a windows VM. I had a Windows 10 VM handy and worked with that. I would suggest something more like XP. 

There is an application available for download from some super skecth-tastic sites, and you need .NET Framework 2.0. So - with the KGB installed on your VM, you can then open this last archive and get your flag.

# References

- [https://wimlib.net/](https://wimlib.net/)
- [https://sourceforge.net/projects/kgbarchiver/](https://sourceforge.net/projects/kgbarchiver/)