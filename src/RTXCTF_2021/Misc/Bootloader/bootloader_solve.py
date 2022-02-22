#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 20:57:51 2021

@author: crr0tz
"""

import socket
from time import sleep
from itertools import combinations
import csv

csv_file = 'results3.csv'
host = '172.18.10.105'
port = 30677

url = (host,port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.2)

passwd = []
lst = [x for x in range(65, 123)]
for j in combinations(lst, 3):
    passwd.append(j)

"""
filtered = []
for j in range(len(passwd)):
    if passwd[j] == i:
        break
 """       

for i in passwd:
    plain_text = bytes(i)
    print(b'trying ' + plain_text)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(url)
    sleep(0.3)
    data = s.recv(180)
    #print(data.decode())
    data = b''
    while 1:
        try:    
            s.send(plain_text)
            sleep(0.1)
            data += s.recv(180)
            print(data)   
        except:
            break
    
    with open(csv_file, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([plain_text,data])

    s.close()

