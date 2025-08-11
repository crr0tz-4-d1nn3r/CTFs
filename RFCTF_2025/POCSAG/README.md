# POCSAG_MSG
30

Virtual

Port 6565 has a pager, you know, like in the nineties.
Physical

This pager can also be found at 444.5 MHz.
Flag

Message from the repeating transmission

## Solution

Install 
```
sudo apt install gqrx sox multimon-ng
```


```
nc -l -u -p 7355 |\
sox -t raw -esigned-integer -b 16 -r 48000 - -esigned-integer -b 16 -r 22050 -t raw - |\
multimon-ng -t raw -a POCSAG512 -f alpha -
```
Decodes to
```
POCSAG512: Address: 1152272  Function: 3 
POCSAG512: Address: 1332025  Function: 3  Alpha:   A kit fox is not a fox kit unless it is a kit fox kit.
POCSAG512: Address: 1011297  Function: 3  Alpha:   INCALERT1018180<SOH><NUL>
```

## Flag
```
A kit fox is not a fox kit unless it is a kit fox kit.
```

# POCSAG_CAP
30
Virtual

Port 6565 has a pager, you know, like in the nineties.
Physical

This pager can also be found at 444.5 MHz.
Flag

Capcode from the repeating transmission


Same proceedure as above - but flag is address
```
1332025
```