# SSH in tunnels
50 pts

SSH through the bastion to the pivot.

IP: 10.218.176.199 User: whistler Pass: cocktailparty

author: @NOPResearcher

## Flag
```
ts{IThoughtWeLostYouOnTheWay}
```
## Solution
```
ssh -J tunneler@104.131.101.182:2222 whistler@10.218.176.199
tunneler
cocktailparty
```

Flag in the header. Has some issues at first with accepting the ssh key

```
.___________. __    __  .__   __. .__   __.  _______  __       _______ .______      
|           ||  |  |  | |  \ |  | |  \ |  | |   ____||  |     |   ____||   _  \     
`---|  |----`|  |  |  | |   \|  | |   \|  | |  |__   |  |     |  |__   |  |_)  |    
    |  |     |  |  |  | |  . `  | |  . `  | |   __|  |  |     |   __|  |      /     
    |  |     |  `--'  | |  |\   | |  |\   | |  |____ |  `----.|  |____ |  |\  \----.
    |__|      \______/  |__| \__| |__| \__| |_______||_______||_______|| _| `._____|
                                                                                    
ts{IThoughtWeLostYouOnTheWay}

Pivot-1:

Some things you can do:

Something is Beaconing to the pivot on port 58671-58680 to ip 10.112.3.199, can you tunnel it back?

scan for the ftp server: 10.112.3.207 user: bishop pass: geese  (Its not where you think it is, also the banner is important)

connect to pivot-2 ip: 10.112.3.12 ssh port: 22 user: crease pass: NoThatsaV

connect to ip: 10.112.3.88 port: 7000, a beacon awaits you
````