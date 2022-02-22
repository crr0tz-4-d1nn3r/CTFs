# Getting Started
Register, login, join team, the usual stuff.

Metasploit provides two VMs -  a kali machine for you to ssh into and an Unbuntu box to attack.

Download your private key. Change the permissions 0600.

## Impressions
This was a well-made and fun CTF. I really liked that each team got their own boxes to play with. While that could be prohibitive for smaller CTFs, it really helped to not be stumbling over someone else on the same box and challenge. 

While some of the problems felt "guessy", the guesses were never too out of scope. If I found myself questioning the guesses - it probably meant that I was taking the wrong approach, using the wrong tool, or just being lazy (tired).

I usually don't do the Web Exploit challenges - my team members are really good at those. Typically I concentrate on Rev, Programming, Crypto, Steg, etc... So this was a nice change and I learned things.

Thanks to the organizers and thanks to the participants that take the time to write up thier solutions. Cheers!

## Init Research

Ran nmap to discover open ports, here is a breif list of those results and some notes of what I got done.
| ip:port | status | notes |
|:---|:---:|:---|
|172.15.41.117:80   | 1 | [4 of Hearts](4_of_Hearts/) |
|172.15.41.117:1080 | - | no clue |
|172.15.41.117:1337 | + | 9 of clubs |
|172.15.41.117:4545 | 8 | [8 of Hearts](8_of_Hearts/)  |
|172.15.41.117:5555 | 2 | [8 of Diamonds](8_of_Diamonds/)  |
|172.15.41.117:6868 | 6 | [6 of Hearts](6_of_Hearts/) |
|172.15.41.117:8080 | 5 | [3 of Spades](3_of_Spades/) |
|172.15.41.117:8092 | - | saltly php |
|172.15.41.117:8101 | - | metasploit module creation |
|172.15.41.117:8123 | 7 | [Black Joker](Black_Joker/) |
|172.15.41.117:8200 | 4 | [6 of Diamonds](6_of_Diamonds/) |
|172.15.41.117:8202 | - | http login page |
|172.15.41.117:8201 | - | http, not nc |
|172.15.41.117:8888 | - | metasploit modules api |
|172.15.41.117:9000 | - | HTTP games ruby website |
|172.15.41.117:9008 | - | unsure , see 9010 |
|172.15.41.117:9007 | 3 | [Red_Joker](Red_Joker/) |
|172.15.41.117:9010 | - | jar file that seems to relate to 9008 |
|172.15.41.117:9009 | + | Ace of Clubs |
|172.15.41.117:9001 | - | http, another ruby query form |


## Challenges tried but did not complete:



### 9 of Clubs
This challenge is found on port 1337. Connect using netcat
```
Welcome to the '9 of Clubs' service.
-------------------------------
Please choose an option:
1. Send contact info
2. Greetings
3. Send feedback
0. Exit
```

Tried some ```eval()``` and buffer overflow attacks. Did not try ```%x``` exploits - which ended up being the right approach. Great writeup on CTFTime's website for this.

### Ace of Clubs
This challenge is on port 9009. SSH into this box and log in as admin
```
kali@kali:~$ ssh admin@172.15.41.117 -p 9009
Welcome to the Ace of Clubs challenge!                                                                            
Login as admin to get started.                                                                                    
admin@172.15.41.117's password:        
```

Made some guesses. Found that the password is ```password```

Output:
```
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 5.4.0-1029-aws x86_64)        
...                                                

Could not chdir to home directory /home/admin: No such file or directory
```

Looking around at some of the directories we have access to, find /etc/ace_of_clubs.png but cannot access permission are read only for root. Need to esculate privs. Also need to get a proper shell
```
perl -e 'exec "/bin/bash";'
```

Sent some time looking at how to do this, but the box is super locked down. Found another file in opt/vpn_connect and searched for what that might be. Turns out - it's the key to getting root.... but I never ran it or dissected it. Wow - what a fool am I.

Good writeup on CTFTime detailing the rest of the solution.

