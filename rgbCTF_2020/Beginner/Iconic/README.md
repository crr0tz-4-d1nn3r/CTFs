README

# Name a more iconic band
411 points, solve #22, 11 hours, 40 minutes after release (2020-07-12 04:40:43)

I'll wait.

The flag for this challenge is all the passwords in alphabetical order, each separated by a single white-space as an MD5 hash in lower case

md5(passwordA passwordB passwordC ...)

Example: if the passwords were "dog" and "cat", the flag would be
rgbCTF{md5("cat dog")}
rgbCTF{b89526a82f7ec08c202c2345fbd6aef3}


~Klanec#3100
data.7z

## Flag
```shell
```

## Solution
Started this one earlier. 1GB when decommpressed. What the heck is this thing? Based on the size I was thinking it was a memory dump. Looked at the first couple bytes in the file - "ELF" ummm? Ghidra? Boy that was a mistake. But it was also obvious that it was not a program. I moved on and solved some easier problems.

When I came back to it later, I remembered that Volitility was a tool that could help. Did some basic research on what to do with the file.
