# Strings
75 points

strings the attached file or maybe you can't, I don't know what I'm doing.

## Flag:
```shell
ts{DidYouUseStringsorMaths}
```

## Solution
Didn't use strings or maths (really). Called strings and saw that the strings.s file was an assebly file. I compiled it and opend in Ghidra, then looked at the hex vales:
```shell
74 73 7b 44 69 64 59 6f 75 55 73 65 53 74 72 69
6e 67 73 6f 72 4d 61 74 68 73 7d
```

Another way to do this is to take the values presented - make them into hex and then decode as ascii. And of course, endianess
```shell
8023554614420534132 = 0x6f596469447b7374 = oYdiD{st
```

