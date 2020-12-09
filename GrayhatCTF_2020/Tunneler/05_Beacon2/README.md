# Beacons annoying
100 pts

Connect to ip: 10.112.3.88 port: 7000, a beacon awaits you

author: @NOPResearcher

## Flag

## Solution
set up the ssh tunnel
```
ssh -D 9050 -J  tunneler@104.131.101.182:2222 whistler@10.218.176.199
tunneler
cocktailparty
```

proxychain into the second pivot
```
proxychains ssh crease@10.112.3.12
NoThatsaV
```

proxychain into the beacon
```
proxychains nc 10.112.3.88 7000

ProxyChains-3.1 (http://proxychains.sf.net)
|S-chain|-<>-127.0.0.1:9050-<><>-10.112.3.88:7000-<><>-OK

I hope you like tunneling, I will send you the flag on a random port... How fast is your tunnel game?
I will send the flag to ip: 10.112.3.199 on port: 33558 in 15 secondsthe flag was sent, I hope
```

we will need one more proxy. Set that first and redo. Open new terminal. gett it ready for next port (this should totally be scripted)
```
proxychains nc 10.112.3.199