README

# Intro
300 points

ssh -p 1337 pwn@54.158.92.212

Password: pwnplayground2020

Flag format: TS{...}

The objective for all pwn challenges is to get the target binary in /CHALLENGES/{NAME}/target to read a flag from /proc/flag. This can be done by:

obtaining a shell and running cat /proc/flag (if the seccomp filter allows it)
using shellcode that performs an open(), read(), write() to read data from /proc/flag
Tips:

Tools on the remote server include python3 and pwntools if you need them
Use nano/vim to transfer scripts
Each ssh connection is a clean jail, don't forget to save your work locally before disconnecting
unset env LINES, unset env COLUMNS, unset env HOME in GDB to make the environment similar to outside of gdb then run env /CHALLENGES/{NAME}/target < payload.txt or env - /CHALLENGES/{NAME}/target < payload.txt or some variation of the environment, since the environment is on the stack.

## flag
```shell

```

## solution
I don't know what I'm doing - just want to start with that. Navigate to /CHALLENGES/intro. Read the README, not much help. strings target? Nothing to interesting, but "main" is named.

```
gdb target
disassemble main
break main
break *(&main+132)
break *(&main+185)
run
c
(waits for input)
```

After putting in input, note that it is stored in RAX, gets moved to rbp - 0x10. Compared to 0? if not =0, jump, otherwise call? So, was not = 0, so it jumped to end. Set a break point for that (above), changed the RAX so it wooldn't jump. Got to the vuln() function. it ran through, but noting printed...
