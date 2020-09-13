README

# baby_mult
50pts

Welcome to reversing! Prove your worth and get the flag from this neat little program!

[program.txt]

## Flag:
```flag
flag{sup3r_v4l1d_pr0gr4m}
```

## Solution

Download text file. It's a bunch of comma seperated values. Values range from 0 to 255. 
```shell
85, 72, 137, 229, 72, 131, 236, 24, 72, 199, 69, 248, 79, 0, 0, 0, 72, 184, 21, 79, 231, 75, 1, 0, 0, 0, 72, 137, 69, 240, 72, 199, 69, 232, 4, 0, 0, 0, 72, 199, 69, 224, 3, 0, 0, 0, 72, 199, 69, 216, 19, 0, 0, 0, 72, 199, 69, 208, 21, 1, 0, 0, 72, 184, 97, 91, 100, 75, 207, 119, 0, 0, 72, 137, 69, 200, 72, 199, 69, 192, 2, 0, 0, 0, 72, 199, 69, 184, 17, 0, 0, 0, 72, 199, 69, 176, 193, 33, 0, 0, 72, 199, 69, 168, 233, 101, 34, 24, 72, 199, 69, 160, 51, 8, 0, 0, 72, 199, 69, 152, 171, 10, 0, 0, 72, 199, 69, 144, 173, 170, 141, 0, 72, 139, 69, 248, 72, 15, 175, 69, 240, 72, 137, 69, 136, 72, 139, 69, 232, 72, 15, 175, 69, 224, 72, 15, 175, 69, 216, 72, 15, 175, 69, 208, 72, 15, 175, 69, 200, 72, 137, 69, 128, 72, 139, 69, 192, 72, 15, 175, 69, 184, 72, 15, 175, 69, 176, 72, 15, 175, 69, 168, 72, 137, 133, 120, 255, 255, 255, 72, 139, 69, 160, 72, 15, 175, 69, 152, 72, 15, 175, 69, 144, 72, 137, 133, 112, 255, 255, 255, 184, 0, 0, 0, 0, 201
```

Suspicious, I used CyberChef for convert decimal charcode values to Hex. Not particularly interesting.

```shell
UH.åH.ì.HÇEøO...H¸.OçK....H.EðHÇEè....HÇEà....HÇEØ....HÇEÐ....H¸a[dKÏw..H.EÈHÇEÀ....HÇE¸....HÇE°Á!..HÇE¨ée".HÇE 3...HÇE.«
..HÇE..ª..H.EøH.¯EðH.E.H.EèH.¯EàH.¯EØH.¯EÐH.¯EÈH.E.H.EÀH.¯E¸H.¯E°H.¯E¨H..xÿÿÿH.E H.¯E.H.¯E.H..pÿÿÿ¸....É
```

Flavor text from problem suggest that this is a program. So, disassembly?
```shell
PUSH RBP
MOV RBP,RSP
SUB RSP,0000000000000018
MOV QWORD PTR [RBP-08],0000004F
MOV RAX,000000014BE74F15
MOV QWORD PTR [RBP-10],RAX
MOV QWORD PTR [RBP-18],00000004
MOV QWORD PTR [RBP-20],00000003
MOV QWORD PTR [RBP-28],00000013
MOV QWORD PTR [RBP-30],00000115
MOV RAX,000077CF4B645B61
MOV QWORD PTR [RBP -38],RAX
MOV QWORD PTR [RBP-40],00000002
MOV QWORD PTR [RBP-48],00000011
MOV QWORD PTR [RBP-50],000021C1
MOV QWORD PTR [RBP-58],182265E9
MOV QWORD PTR [RBP-60],00000833
MOV QWORD PTR [RBP-68],00000AAB
MOV QWORD PTR [RBP-70],008DAAAD
MOV RAX,QWORD PTR [RBP-08]
IMUL RAX,QWORD PTR [RBP-10]
MOV QWORD PTR [RBP-78],RAX
MOV RAX,QWORD PTR [RBP-18]
IMUL RAX,QWORD PTR [RBP-20]
IMUL RAX,QWORD PTR [RBP-28]
IMUL RAX,QWORD PTR [RBP-30]
IMUL RAX,QWORD PTR [RBP-38]
MOV QWORD PTR [RBP-80],RAX
MOV RAX,QWORD PTR [RBP-40]
IMUL RAX,QWORD PTR [RBP-48]
IMUL RAX,QWORD PTR [RBP-50]
IMUL RAX,QWORD PTR [RBP-58]
MOV QWORD PTR [RBP-00000088],RAX
MOV RAX,QWORD PTR [RBP-60]
IMUL RAX,QWORD PTR [RBP-68]
IMUL RAX,QWORD PTR [RBP-70]
MOV QWORD PTR [RBP-00000090],RAX
MOV EAX,00000000
LEAVE
```

Ok, that makes since, "baby multiply". So, what's happening? Stores values in various variables. Then multiply a few things at a time. Then leave? So, what's thje result. Four variables, that when decoded as ascii give the flag:
```python
var08 = 0x0000004F
var10 = 0x000000014BE74F15
var18 = 0x00000004
var20 = 0x00000003
var28 = 0x00000013
var30 = 0x00000115
var38 = 0x000077CF4B645B61
var40 = 0x00000002
var48 = 0x00000011
var50 = 0x000021C1
var58 = 0x182265E9
var60 = 0x00000833
var68 = 0x00000AAB
var70 = 0x008DAAAD

var78 = var08 * var10
var80 = var18*var20*var28*var30*var38
var88 = var40*var48*var50*var58
var90 = var60*var68*var70

parts = [var78, var80, var88,var90]
for part in parts:
    print(bytes.fromhex(hex(part)[2:]).decode('ascii'), end='')
```