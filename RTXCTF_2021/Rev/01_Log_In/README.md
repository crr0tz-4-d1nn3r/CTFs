#  Log-in
100

We discovered this binary that appears to belong to a login prompt on the attacker's server, we've tried reverse engineering it but none of the data we're seeing makes sense.

Can you figure out how to login to the service?
```
nc 172.18.10.105 39129
```

[client_login](client_login)

# Flag
```
RTXFLAG{p4ck3rs_suck_but_that_doesnt_matter_not_talking_about_greenbay}
```

# Solution
This si one that Plummdog started. When I peeked in, he was working through tracing the program. The problem is - IDA, Ghidra, GDB won't touch it. It's missing section headers
```
$ file client_login 
client_login: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, missing section headers
$ readelf -h client_login 
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 03 00 00 00 00 00 00 00 00 
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - GNU
  ABI Version:                       0
  Type:                              EXEC (Executable file)
  Machine:                           Advanced Micro Devices X86-64
  Version:                           0x1
  Entry point address:               0x7bfb98
  Start of program headers:          64 (bytes into file)
  Start of section headers:          2271635 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           56 (bytes)
  Number of program headers:         6
  Size of section headers:           64 (bytes)
  Number of section headers:         33
  Section header string table index: 32
readelf: Error: Reading 2112 bytes extends past end of file for section headers
```

It would run though. Program calls for the user to login.
```
$ ./client_login 
Runing........
The goal is simple... login.
```

Should we just trying some fuzzing? Nothing on the first input. But... it looks like it takes two inputs - something I vastly overlooked. I just thought I had to press ENTER again. Bad hacker! Never overloook something like this. If I had just tried:
```
$ ./client_login 
Runing........
The goal is simple... login.aaaaaaaaaaaaaaaaa
qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
RTXFLAG{Dummy flag inserted here}Fail.
```

But we weren't there yet. Radar2 will read it. So he had begun picking it apart there. It had some very strange behaviour. I believe he said something like "1 million plus xors." Custom packer?!?

He ended up dumping the program from memory. At least Ghidra and IDA would work with it.
[core.3087](core.3087)

Started tracing the function where we found the strings that show on the command line during exectuion.
```
undefined8 FUN_00400fdd(void)

{
  undefined8 uVar1;
  ulong uVar2;
  undefined local_98 [32];
  undefined local_78 [32];
  undefined local_58 [63];
  char local_19;
  
  local_19 = '\0';
  FUN_004b8760(s_The_goal_is_simple..._login._005617e9);
  FUN_004327c0(local_78);
  FUN_00402b70(&DAT_007bdc80,local_78);
  uVar1 = FUN_00433f60(local_78);
  uVar2 = thunk_FUN_0040059e(uVar1);
  if (0x13 < uVar2) {
    FUN_004ad3b0(0);
  }
  uVar2 = thunk_FUN_0040059e(local_58);
  if (0x14 < uVar2) {
    FUN_004ad3b0(0);
  }
  FUN_004327c0(local_98);
  FUN_00402b70(&DAT_007bdc80,local_98);
  uVar1 = FUN_00433f60(local_98);
  thunk_FUN_00400516(local_58,uVar1);
  if (local_19 != '\0') {
    FUN_004b8760(s_RTXFLAG{Dummy_flag_inserted_here_00561808);
  }
  FUN_004b8760(s_Fail._0056182a);
  FUN_004328c0(local_98);
  FUN_004328c0(local_78);
  return 0;
}
```

A bunch of functions are for getting input and looking at string lengths. The thing that stands out to me is local_19
```
local_19 = '\0';
...
if (cStacklocal_1925 != '\0') {
    FUN_004b8760(s_RTXFLAG{Dummy_flag_inserted_here_00561808);
  }
...
```
  uVar2 = thunk_FUN_0040059e(local_58);
This variable is never touched except at initialization and check. There must be some way of corrupting the value. The memory is at rdp - 0x19 and the second user input at rdp - 0x50. That means a string of length 0x58 - 0x19 + 1 = 64 to overflow the input buffer and set local_19 to something - anything - to pass the check and get the flag.
```
$ ./client_login 
Runing........
The goal is simple... login.aaaaaa
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
RTXFLAG{Dummy flag inserted here}Fail.$ ./client_login 
Runing........
The goal is simple... login.aaaaaa
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
RTXFLAG{Dummy flag inserted here}Fail.
```

So - yeah, could have totally fuzzed that - and quickly. But, by taking the long way, we found a custom packer. That's pretty cool.

# References
- [https://ghidra-sre.org/](https://ghidra-sre.org/)
- [https://rada.re/n/](https://rada.re/n/)
- [https://gist.github.com/williballenthin/6857590dab3e2a6559d7](https://gist.github.com/williballenthin/6857590dab3e2a6559d7)