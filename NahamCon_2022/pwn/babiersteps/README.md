# 
# Solution
Initial testing shows we may have a buffer overflow. Running the program in gdb info func shows a "win" function and set break at main+48 (this is right after call to scanf). Also opening in ghidra.

the win function should give us a shell
```
void win(void)
{
  execve("/bin/sh",(char **)0x0,(char **)0x0);
  return;
}
```

And it looks like the buffer is 112 bytes
```
undefined8 main(void)
{
  undefined local_78 [112];
  
  puts("Everyone has heard of gets, but have you heard of scanf?");
  __isoc99_scanf(&DAT_00402049,local_78);
  return 0;
}
```

So create the payload with (112+8) * 'a' and then the address of win.

# Flag
```
flag{4dc0a785da36bfcf0e597917b9144fd6}
```