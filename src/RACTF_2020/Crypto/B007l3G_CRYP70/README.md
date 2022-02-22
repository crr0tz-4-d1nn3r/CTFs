# B007l3G CRYP70
350 points

Connet to service running (provided IP and port).

While doing a pentest of a company called MEGACORP's network, you find these numbers laying around on an FTP server: 

41 36 37 27 35 38 55 30 40 47 35 34 43 35 29 32 38 37 33 45 39 30 36 27 32 35 36 52 72 54 39 42 30 30 58 27 37 44 72 47 28 46 45 41 48 39 27 27 53 64 32 58 43 23 37 44 32 37 28 50 37 19 51 53 30 41 18 45 79 46 40 42 32 32 46 28 37 30 43 31 26 56 37 41 61 68 44 34 26 24 48 38 50 37 27 31 30 38 34 58 54 39 30 33 38 18 33 52 34 36 31 33 28 36 34 45 55 60 37 48 57 55 35 60 22 36 38 34.

Through further analysis of the network, you also find a network service running. Can you piece this information together to find the flag?

## Flag
Also didn't write this one down. Still getting the hang of documenting my procecss as I go.

## Solution
For crypto/B007l3G CRYP70 I didn't code. I used Excel. Server returns 4 numbers for each character sent. It will also send different sets of numbers for the same character. However, each time, the sum of the numbers is the same. The values correlated strongly to ascii, but with an offset and in descending value. I used Excel to create a map, and used a VLOOKUP to map the sum of 4 number groups:

41 36 37 27 -> 41 + 26  + 37 + 27 = 141 -> 'r'

Didn't save the spreadsheet. Again, new at this CTF thing.
