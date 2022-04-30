# Prisoner
Have you ever broken out of jail? Maybe it is easier than you think! 


# Solution
Start an instance and ssh into box using instructions provided.
```
  _________________________
     ||   ||     ||   ||
     ||   ||, , ,||   ||
     ||  (||/|/(\||/  ||
     ||  ||| _'_`|||  ||
     ||   || o o ||   ||
     ||  (||  - `||)  ||
     ||   ||  =  ||   ||
     ||   ||\___/||   ||
     ||___||) , (||___||
    /||---||-\_/-||---||\
   / ||--_||_____||_--|| \
  (_(||)-| SP1337 |-(||)_)
          --------

Hello prisoner, welcome to jail.
Don't get any ideas, there is no easy way out!
```

* Try things like ls, pwd, whoami, -> not working
* Try things like long inputs -> nope
* Tried eval(), dir(), ... -> nope
* Tried Ctrl+c, Ctrl+A B (or something) and got a python terminal?

So, what do we do? Tried dir(), eval(), ... Finally settled on open():
```
>>> with open('flag.txt','r') as fh:
...   print(fh.readlines())
... 
['flag{c31e05a24493a202fad0d1a827103642}\n']
>>> 

```


# Flag
```
flag{c31e05a24493a202fad0d1a827103642}
```