# Crash Override
Remember, hacking is more than just a crime. It's a survival trait. 

Attachments: [crash_override](crash_override), [crash_override.c](crash_override.c), [Makefile](makefile)

# Solution
Open the c file. Looks like a buffer overflow to trigger a segfault and get the win.
Need a buffer of 2048 bytes and another 8 bytes to overwrite the base pointer and 1 more to currupt the instruction pointer on return. To test this locally:
```
python -c "print('a'*(2048+8+1))"
```
Take this output and use in when running the program.

Works. Try on server.

# Flag
```
flag{de8b6655b538a0bf567b79a14f2669f6}
```