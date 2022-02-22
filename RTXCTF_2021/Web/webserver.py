#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 22:43:51 2021

@author: crr0tz
"""

#!/usr/bin/env python

import asyncio
import websockets

async def hello(websocket, path):
    waiting = True
    while waiting:
        with open('payload.jpg','rb') as fh:
            data = bytearray(fh.read())
        
        data = base64.b64encode(data)
        await websocket.send(data)
        waiting = False

start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
