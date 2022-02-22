#  ltrace-easy
100 pts

Can you run the binary?

You may have to trace it or something.

[LTRACE-EASY](ltrace-easy)

author: @nopresearcher

## Flag
```shell
ts{whydidyouevenrunit}
```

## Solution
Download binary. file command lets you know it's an ELF file, strings shows nothing interesting. Open in Ghidra. Main starts at 0x001011a5. Some interesting byte arrays are being allocated. Explored those. 
