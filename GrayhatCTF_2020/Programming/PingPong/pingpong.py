import socket
import random
from time import sleep

numbers=[15]
host='104.131.127.22'
port=2346

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, int(port)))
data = s.recv(5000)
data = s.recv(5000)
msg = 'T'
while data :
    s.sendall(data)
    data = s.recv(5000)
    msg += data.decode('ascii').strip('\n')
    if '}' in msg:
        break

print (msg)