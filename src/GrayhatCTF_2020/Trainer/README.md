# Level 1
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
```
ssh level0@167.71.187.239
level0
cat level1_password
```
We are told that the password for the next level is in the user's directory. There is a file called level1_password. cat that out to get the flag


# Level 2

## flag:
```shell
943430e07fd566bc96aa05fca3c96e48
```

## solution:
```
ssh level1@167.71.187.239
4202c26842398c1d0772ed9eed195113

```
ssh into level1 using the previous flag. Again password is in the user directory, but we need to dig. There is a directory, some_directory. cd into that. ls tells us ther is a level2_password file. cat that.



# Level 3

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


## flag:
```shell
192
```

## solution
```
ssh level10@167.71.187.239 
955830
```
For this level you are given a log file from the program fail2ban.  Fail2ban is used monitor log files for suspicious activity like too many failed logins.  It is commonly deployed for use with Apache or SSH.  After a configured number of attempts it will create an iptables (linux firewall) rule to block the ip from communicating with the device for a period of time.

The log file is located in your home directory and is called fail2ban.log.  The password to level 11 is the number of times 112.85.42.94 was banned.



# Level 12

## flag:
```shell
0982e2a869857644074d06b1a4fd1bea
```

## solution
```
ssh level11@167.71.187.239 
192
grep -x '.\{32\}' md5find 
```
For this level you are given a file that contains the password to the next level.  The password is a md5 hash.  Research md5 hashes and find it in the file.
An MD5 hash is 32 characters long. Lets see how many lines in the md5find file are




# Level 13
## flag
```
f4736e1eb28b1d9055c5f5d58a49b5a6
```
## solution
```
ssh level12@167.71.187.239
0982e2a869857644074d06b1a4fd1bea
find / -perm -4000 -type f 2>/dev/null
cat /usr/sbin/mysecret
cat /home/level13/mypassword.txt 
```
For this level you are going to find SUID and SGID binaries in common locations.  This is a common privilege escalation technique seen in CTFs and real world.  Remember the user you are looking to escalate privileges to is level13. 

SUID (Set owner User ID up on execution) - Is a special file permission for executable files which enables other users to run the file with effective permissions of the file owner. 
SGID is a special file permission that also applies to executable files and enables other users to inherit the effective GID of file group owner.

getting a list of files with interesting permissions shows a result in /usr/sbin/mysecret
this is a program, cat it out, see a mention to a password file. Cat that as well. get the password!


# Level 14
## flag
```
0ea027e3835aa87a4a47465321c5fe75
```
## solution
```
ssh level13@167.71.187.239
f4736e1eb28b1d9055c5f5d58a49b5a6
printenv
```

For this level you are going to familiarize yourself with environment variables.  They are used for a wide variety of applications.  Specifically, they can be used for docker and cloud providers to store credentials.  They password to level 14 is is the one that ends with ID.

printenv will list all the environment variables. 
```
...
AWS_ACCESS_KEY_ID=0ea027e3835aa87a4a47465321c5fe75
...
```


# Level 15
## flag
```
4.19
```
## solution
For this level you are going to familiarize yourself with the kernel version.  We are just looking for the Kernel and Major version (the first two sets of numbers) example: if the version is 2.62.26.1 the password will be 2.62

Understanding Kernel versions can help when search for exploits with tools like searchsploit or exploitdb (Sorry, there isn't any kernel exploits for this box, I hope)

```
ssh level14@167.71.187.239
0ea027e3835aa87a4a47465321c5fe75
uname -v
```

#1 SMP Debian 4.19.132-1 (2020-07-24)


# Level 16
## flag
```
Debian
```
## solution
```
ssh level15@167.71.187.239
4.19
hostnamectl
```

For this level you are going to familiarize yourself with the distro version.  We are just looking for the distro name.  example: Fedora 31, then the password would be Fedora

Understanding distro versions can help when searching for exploits with tools like searchsploit or exploitdb (Sorry, there isn't any exploits for this distro, I hope)


# Level 17
## flag
```
6b39034a8045ed996a436f8d09031522
```
## solution
```
ssh level16@167.71.187.239
Debian
cat .bashrc 
```

we get a list of alieses used in this profile, including the ssh password


# Level 18
## flag
```
9a42b1822710d790a393800f2896a8f7
```
## solution
```
ssh level17@167.71.187.239
6b39034a8045ed996a436f8d09031522
cat .viminfo.swp
```

For this level you are going to familiarize yourself with user artifacts.  Look in this user's home directory to see if there are any files left behind that may contain useful information.

cat out the users vim swap file

# Level 19
## flag
```
b06a246b0646b337f319316b9232151c
```
## solution
```
ssh level18@167.71.187.239
9a42b1822710d790a393800f2896a8f7
ls -la
cat .bash_history 
```

For this level you are going to continue familiarizing yourself with user artifacts.  Look in this user's home directory to see if there are any files left behind that may contain useful information.

list out the files. there is a bash history file, cat that.

# Level 20
## flag
```
5cf82d972614f73422f899f90cfce80f
```
## solution
```
ssh level19@167.71.187.239
b06a246b0646b337f319316b9232151c
cat .ssh/level20_id_rsa 
scp level19@167.71.187.239:~/.ssh/level20_id_rsa .
b06a246b0646b337f319316b9232151c
ssh -i level20_id_rsa level20@167.71.187.239
cat level20_password

```

For this level you are going to continue familiarizing yourself with user artifacts.  Look in this user's home directory to see if there are any files left behind that may contain useful information.

This level is focused on user artifacts and in particular ssh keys.  The user has a private ssh key to what appears to be level20.  You can't ssh to yourself so lets try and figure out how to get this back to you.  You can use scp to securely copy it back or you can cat it to the screen and copy/paste it to your local machine.  Then just ssh into level20 and cat the password.

This level is focused on user artifacts and in particular ssh keys.  The user has a private ssh key to what appears to be level20.  You can't ssh to yourself so lets try and figure out how to get this back to you.  You can use scp to securely copy it back or you can cat it to the screen and copy/paste it to your local machine.  Then just ssh into level20 and cat the password.


# Level 21
## flag
```
65230da2ead4ba2ed76ee2605cadcd4d
```
## solution

For this level you are going to continue familiarizing yourself with user artifacts.  Look in this user's home directory to see if there are any files left behind that may contain useful information.

had trouble extracting the backup archive, so I downloaded it.
```
scp level20@167.71.187.239:~/backup.tgz .
5cf82d972614f73422f899f90cfce80f
tar -xvf backup.tgz
```

# Level 22
## flag
```
643b2616b33de99b179c33950970d519
```
## solution
```
ssh level21@167.71.187.239
65230da2ead4ba2ed76ee2605cadcd4d
ls -la
file mybackup 
scp level21@167.71.187.239:~/mybackup .
65230da2ead4ba2ed76ee2605cadcd4d
bunzip2 -d mybackup
cat mybackup.out
```

For this level you are going to continue familiarizing yourself with user artifacts.  Look in this user's home directory to see if there are any files left behind that may contain useful information.

mybackup looks like a compressed file (BZ)
pull it down and look at it
