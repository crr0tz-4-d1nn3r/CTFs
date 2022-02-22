# Another Pivot
75 pts

Connect to the second pivot

IP: 10.112.3.12 User: crease Pass: NoThatsaV

## Flag
```
ts{TunnelsInTunnelsInTunnels}
```

## Solution

ssh into whistler
```
ssh -D 9050 -J  tunneler@104.131.101.182:2222 whistler@10.218.176.199
tunneler
cocktailparty
```
from another terminal on host, copy .ssh/authorized_keys
```
proxychains scp whistler@10.218.176.199:~/.ssh/authorized_keys .
```
Now ssh into crease
```
proxychains ssh crease@10.112.3.12
NoThatsaV

.___________. __    __  .__   __. .__   __.  _______  __       _______ .______      
|           ||  |  |  | |  \ |  | |  \ |  | |   ____||  |     |   ____||   _  \     
`---|  |----`|  |  |  | |   \|  | |   \|  | |  |__   |  |     |  |__   |  |_)  |    
    |  |     |  |  |  | |  . `  | |  . `  | |   __|  |  |     |   __|  |      /     
    |  |     |  `--'  | |  |\   | |  |\   | |  |____ |  `----.|  |____ |  |\  \----.
    |__|      \______/  |__| \__| |__| \__| |_______||_______||_______|| _| `._____|
                                                                                    
ts{TunnelsInTunnelsInTunnels}

Pivot-2:

Not all SSH servers allow tunnels, so you have to get creative sometimes.

Socat is here if you need it.

There is a samba server at 10.24.13.10, find a flag sitting in /

```