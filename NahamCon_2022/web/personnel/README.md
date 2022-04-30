# Personnel
A challenge that was never discovered during the 2021 Constellations mission... now ungated :) 

Attachment: [app.py](app.py)

# Solution
Download attachment. Flask website. flag is appended to the end of a list of users. Using re to search, but pattern needs to end in a [a-z] characteror what ever the user decided. So we look for and end of line and anything after. Adding an uppercase letter at the start of input as it will get stripped off and protect the rest.

```
A\n.+
```

# Flag
```
flag{f0e659b45b507d8633065bbd2832c627}
```