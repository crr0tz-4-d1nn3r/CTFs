# Babysteps
Become a baby! Take your first steps and jump around with BABY SIMULATOR 9000! 

# Solution

Download attachments. Open the c file. Looks like there is a buffer overflow in the name. No "win" function, so may need to get a shell.

looking at a few bits of info:
```
└─$ file babysteps  
babysteps: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=23b7b1945e8ce3847c586e16d9ccfb70fe7b6973, for GNU/Linux 3.2.0, not stripped

└─$ ldd babysteps
        linux-gate.so.1 (0xf7ed6000)
        libc.so.6 => /lib/i386-linux-gnu/libc.so.6 (0xf7cc8000)
        /lib/ld-linux.so.2 (0xf7ed8000)

└─$ checksec --file=babysteps       
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified  Fortifiable     FILE
Partial RELRO   No canary found   NX disabled   No PIE          No RPATH   No RUNPATH   59) Symbols       No    0 1babysteps

```
Looks like stack is executable. We should be able to put shell code in the buffer and then jump to it. Need a gadget. Noticed that the input is in eax and we have a jump eax gadget available.

```
[*] Switching to interactive mode

$ ls
babysteps
bin
dev
etc
flag.txt
lib
lib32
lib64
libx32
usr
$ cat flag.txt
flag{7d4ce4594f7511f8d7d6d0b1edd1a162}
$  

```


# Flag
```
flag{7d4ce4594f7511f8d7d6d0b1edd1a162}
```
