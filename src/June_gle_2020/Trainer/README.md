# Level 1
10 points

login to the linux trainer:

ssh level0@xxx.xxx.xxx

username: level0 password: level0

The password will be the login to level1

Note: Not the standard flag format

## flag:
```shell
4202c26842398c1d0772ed9eed195113 
```

## solution:
We are told that the password for the next level is in the user's directory. There is a file called level1_password. cat that out to get the flag


# Level 2
10 points

## flag:
```shell
943430e07fd566bc96aa05fca3c96e48
```

## solution:
ssh into level1 using the previous flag. Again password is in the user directory, but we need to dig. There is a directory, some_directory. cd into that. ls tells us ther is a level2_password file. cat that.



# Level 3
10 points

## flag:
```shell
2cadca6148093c403d82396252b8c4db
```

## solution
ssh into level 2. Again password is in the user directory, but we need to dig. There is a directory and a compiled c program? 
```shell
file a.out
```

It's empty. so dir it is. dir has another_dir. Cd into that. and another... couple more cds and level3_password. 



# Level 4
10 points

## flag:
```shell
72f6af6b0005adb15fbc91e1b140115f
```

## solution
```
ssh level3@167.71.187.239
```

The password for the next level is in this user's home directory, but you might not see it at first.
```
ls -la
```

.level4_password shows up as a hidden file. cat it.


# Level 5
10 points

## flag:
```shell
7b6c2552940f47a27fbd729ae0e2893c
```

## solution
```
ssh level4@167.71.187.239
```
Same as above, but in a hidden directory


# Level 6
10 points

## flag:
```shell
7cb1963d316b9a302cf6c204d35b7302
```

## solution
```
ssh level5@167.71.187.239
```
For this level the password is in level6's home directory.  Due to a persmissions error, the level5 user can access it.  Think about the directories you have already seen and what file name patterns.
using ls to look at contents of /home/level6 shows a level6_password file, cat it.



# Level 7
10 points

## flag:
```shell
RG8geW91IGV2ZW4gbGlmdCBicm8g
```

## solution
```
ssh level6@167.71.187.239 
```
The password for the next level is in this user's home directory, however this time there are too many directories to manually dig through.  For this level you will need the find command and search for a file that has pass in the title.
```
level6@trainer:~$ find . -name "level7*"
```
provides the directory for the file you need. cat it.


# Level 8
10 points

## flag:
```shell
bGV0J3MgZmluZCBzb21ldGhpbmcg
```

## solution
```
ssh level7@167.71.187.239 
```
The password for the next level is in the password_directory.  For this level though, all files are exactly the same size.  You should look through each file to find the one that contains the password.
```shell
grep -v 'This is just some text that is the same file size for you' ./*
```
There is probably an option that can clean this up, but it get's the flag


# Level 9
10 points

## flag:
```shell
96ab15e954f1267ea04c35de2d771c2b
```

## solution
```
ssh level8@167.71.187.239 
```
For this level the password is in an executable hidden in one of these sub-directories.  When you run the executable it will print out the flag.  To run the executable type: ./executable
```
find . -executable -type f
```
show a file ./dir24/subdir13/level9_password. run it


# Level 10
10 points

## flag:
```shell
955830
```

## solution
```
ssh level9@167.71.187.239 
```
First a bit of history.  RockYou was a social media site that suffered a security breach in 2009, losing 32 million passwords.  They were storing all the user credentials in plain text in their database.  At the time this was the largest breach of passwords and allowed for academic research and password analysis with real data.  These passwords were eventually organized into a password list that is commonly used for cracking passwords.  

For this level we want to find the line number in the rock you wordlist where the password "evilhacker" is found.  That line number is the password for level 10.  The wordlist can be found at /usr/share/wordlists/rockyou.txt (it's in the same place on kali too) Grep uses a 1-based numbering system meaning the first line is 1 and not 0.

```
grep -n "evilhacker" /usr/share/wordlists/rockyou.txt
```


# Level 11
10 points

## flag:
```shell
192
```

## solution
```
ssh level10@167.71.187.239 
```
For this level you are given a log file from the program fail2ban.  Fail2ban is used monitor log files for suspicious activity like too many failed logins.  It is commonly deployed for use with Apache or SSH.  After a configured number of attempts it will create an iptables (linux firewall) rule to block the ip from communicating with the device for a period of time.

The log file is located in your home directory and is called fail2ban.log.  The password to level 11 is the number of times 112.85.42.94 was banned.



# Level 12
10 points

## flag:
```shell
0982e2a869857644074d06b1a4fd1bea
```

## solution
```
ssh level11@167.71.187.239 
```
For this level you are given a file that contains the password to the next level.  The password is a md5 hash.  Research md5 hashes and find it in the file.
An MD5 hash is 32 characters long. Lets see how many lines in the md5find file are this lonk
```shell
grep -x '.\{32\}' md5find 
```
only one.



