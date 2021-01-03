# Don't be salty
20

Our l33t hackers hacked a bulletin board and gained access to the database. We need to find the admin password.

The user's database info is:

Username:admin

Passwordhash:2bafea54caf6f8d718be0f234793a9be

Salt:04532@#!!

We know from the source code that the salt is put AFTER the password, then hashed. We also know the user likes to use lowercase passwords of only 5 characters long.

The flag is the plaintext password.

## Flag
```
brute
```

## Solution
Hashcat. Create a file of the form ```<hash>:<salt>``` as such:
```
2bafea54caf6f8d718be0f234793a9be:04532@#!!
```

I guessed that the hash was an md5 (length, characterset,...) and given that we know the form ```<pass><salt>``` and then hashed and we know that possible length and character set of the password use a brute force attach (-a 3) with the pattern ?l?l?l?l?l and specify the form (-m 10)

```
hashcat -m 10 -a 3 saltedhash ?l?l?l?l?l
```

See [https://hashcat.net/wiki/doku.php?id=hashcat](https://hashcat.net/wiki/doku.php?id=hashcat) for details.