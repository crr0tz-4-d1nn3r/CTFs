# Scan me
10 points

Can you solve this scan puzzle?

It could be handy to hide messages

![qr-code.png](qr-code.png)

## Flag:
```
brixelCTF{m4st3r_0f_sc4n5}
```

# Solution
Decoding the QR code provides a link to a website. Decoding can be done with many different applications. I used python library called pyzbar.
```
http://www.timesink.be/qrcode/flag.html
```

This website has another bar code, and another, and another. Wasn't sure how far this rabbit hole was going to go, so I continnued with pyhthon. Unfortunatly, the last bar code, which is a PDF417, is not readable by the pyzbar library. I tried using a homebrew method I found on Github, but didn't work. Ended up just using an online service (with no API).
