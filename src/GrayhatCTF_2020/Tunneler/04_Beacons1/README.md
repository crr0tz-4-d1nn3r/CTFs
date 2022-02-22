# Beacons everywhere
75 pts

Something is Beaconing to the pivot on port 58671-58680 to ip 10.112.3.199, can you tunnel it back?

NOTE: IT IS THE SAME ON EACH PORT ONLY USE ONE PORT AND REMOVE YOUR TUNNEL WHEN YOU ARE DONE

author: @NOPResearcher

## Flag
```
ts{GreatFirstReverseTunnel}
```

## Solution
set up bound port to the iptunneler
```
ssh -D 9050 tunneler@104.131.101.182 -p 2222
tunneler
```

in another terminal on host
```
proxychains firefox 10.174.12.14
```