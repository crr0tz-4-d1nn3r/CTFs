# Time Traveler
398

After you found the location of the attackers we were able to infilitrate their warehouse. However, by the time we got there it seems they'd relocated and only left behind a piece of hardware with a label on it "botnet tests" we're not sure what they were using it for but there's no video output interfaces just an ethernet port and what we've identified as a UART header.

After connecting to the ethernet port on the device it seems to be tossing out random data as it runs, we're not sure how to make sense of it yet but. We were able to dump the binary off the hardware itself and have attached it, maybe you can reverse engineer it and make sense of what's going on? All we know is that it's based on time.

    nc 172.18.10.105 46623

# Flag
```
RTXFLAG{th1s_fl4g_1s_g0ing_t0_$uck_to_extr4ct_t1m3d_dr0ping}
```

# Solution
So this was another one that Chris was working on that I jumped into about half-way. Chis jumped into the chat
```
Hey - you do math-y things right?
```

He had traced out a function and came to an XOR operation and wanted a sanity check. Could we solve for WTFINT (his name not mine)
```
(tm_ptr->tm_sec + WTFINT) ^ tm_ptr->tm_min
```

I said - sure, XOR is it;s own inverse. Thus
```
if result = (tm_ptr->tm_sec + WTFINT) ^ tm_ptr->tm_min
then WTFINT = (result ^  tm_ptr->tm_min) - tm_ptr->tm_sec 
```

So - now I need to catch up. What does the service do when you connect? It prints the time and leaks some data:
```
== proof-of-work: disabled ==
The current time is - 18:18:49
leak is: 0x21
```

What Chris had found was 
```
WTFINT = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::c_str();

sprintf(acStack24,"%02X",(uint)*(byte *)(tm_ptr->tm_sec + WTFINT) ^ tm_ptr->tm_min);

std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::append((char *)curtimeis-local);

__s = (char *)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::c_str();

puts(__s);
```

But something was bugging him - WTFINT was a string - not an int. So what was getting added?

This is just how array indexing works in dissassembled code. Thus
```
tm_ptr->tm_sec + WTFINT
```
is just 
```
WTFINT[tm_ptr->tm_sec]
```

What the code is doing is using the seconds of the time value to index into a character array. It then XORs the character with the minutes and outputs the result.

So we both cobbled together some python and went forth to get the flag.
