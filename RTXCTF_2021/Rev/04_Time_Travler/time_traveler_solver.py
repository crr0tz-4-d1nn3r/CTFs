#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
from time import sleep

host = '172.18.10.105'
port = 46623

url = (host,port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)

flag = [' ']*100

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(url)
    sleep(0.5)
    data = s.recv(1024).decode()
    print(data)

    lines = data.split('\n')
    
    timet = lines[1].strip().split(':')
    tm_sec = int(timet[2])
    tm_min = int(timet[1])
    
    leak = int(lines[2].split(':')[1].strip(),16)

    print(tm_sec)
    print(tm_min)
    print(leak)

    r = (leak ^ tm_min)
    flag[tm_sec] = chr(r)
    print(''.join(flag))
    sleep(0.5)