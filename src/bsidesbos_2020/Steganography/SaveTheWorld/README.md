# Saving the World
452

Sometimes I dream of saving the world. Saving everyone from the invisible hand, the one that brands us with an employee badge, the one the forces us to work for them, the one that controls us every day without us knowing it. But I can't stop it. I'm not that special. I'm just anonymous. I'm just alone.

Download the file below.


# Flag
```shell
flag{take_care_of_whiterose}
```

# Solution
Download the file and open to view. Looks like and ad with some interesting numbers. Looked like character values A=1 .. Z = 26.
```shell
6 2 26 8 16 21 17 18 3 18 1 17 6 8 3 2 1 14 5 18 17 10 21 18 18 25 15 14 5 5 2 10 20 25 14 13 18 17 10 22 7 21 5 14 22 1 10 14 7 18 5 15 18 6 22 17 18 7 21 18 10 21 22 7 18 16 21 22 16 24 18 1 6 7 21 18 3 14 6 6 10 2 5 17 22 6 7 10 18 25 25 22 16 24 25 2 6 18 6 16 7 2
```

But decoded didn't look like much...
```shell
fbzhpuqrcraqfhcbanerqjurryoneebjtynmrqjvguenvajngreorfvqrgurjuvgrpuvpxrafgurcnffjbeqvfgjryyvpxybfrfpgb
```

Tried a couple things like xor and sub. Ended up on ROT13:
```shell
somuchdependsuponaredwheelbarrowglazedwithrainwaterbesidethewhitechickensthepasswordistwellicklosescto
```
Cleaned up, this reads "so much depends upon a red wheel barrow glazed with rain water beside the white chickens the password is twellicklosescto"

Password? Interesting. Lets see what steghide has to say:
```shell
kali@kali:~/Desktop$ steghide --info menu.jpg 
"menu.jpg":
  format: jpeg
  capacity: 6.5 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase: 
  embedded file "flag.txt":
    size: 29.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
```
Embedded file? Extract it please
```shell
kali@kali:~/Desktop$ steghide extract -sf menu.jpg -p twellicklosescto 
wrote extracted data to "flag.txt".
```

Open the file and get your flag.
