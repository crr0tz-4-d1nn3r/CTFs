# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 17:41:03 2020

@author: cruffo
"""

from Crypto.Cipher import DES

with open('ciphertext', 'rb') as handle:
	ct = handle.read()
    
iv = b'13371337'
key = bytes.fromhex('1F1F1F1F0E0E0E0E')

des = DES.new(key, DES.MODE_OFB, iv)
pt = des.decrypt(ct)
print(pt.decode())