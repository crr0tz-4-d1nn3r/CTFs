import subprocess
import struct

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
base_name = '000000000000'
for i in range(62*4):
    seed = chars[i//(63*2)] + chars[i//(63)] + chars[i%62]
    guess = base_name + seed
    print(guess)
    with subprocess.Popen(['/home/kali/Repos/CTFs/TAMUCTF_2022/Pwn/Lucky/lucky/lucky'], 
                stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
        print(str(process.pid))
        process.communicate(guess.encode())
        out = process.communicate()[0]
        if 'Better luck next time!' not in out.decode():
            break
# 000000000000bd9