# Baseball
50

I found this baseball... but... it doesn't really look like a baseball?

Download the file below.

[baseball](baseball)

# flag
```shell
flag{wow_you_hit_a_homerun_and_really_ran_the_bases_there}
```

# Solution
Opening the file - it appears to be a base encoded string.

Trial-n-error...
came acrosse this particular combination:
from base64 -> from base32 -> from base 58 -> flag.
[https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)From_Base32('A-Z2-7%3D',true)From_Base58('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',true)&input=VHpSYVZVTlZNbFJOUlRSSVFUWk1TRkJHV2tkVE5WcFRTelZaVlUxWlNsbElRazVFUjAwelJFZEtUa2hCVlRKV1NrSkhWa05XTWxsUFJsVkZTek15UkU5R1RVVk5Na05hUjBZMVJVMVZVbHBOVWxOSFMxSlNXRTlDUTFWVlUxcFpTazR5U0VGV1ZGVlBWVEpHUXpKRFYwMDBXbFV5VVZOSFNscEJWRk5OVVQwPQ](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)From_Base32('A-Z2-7%3D',true)From_Base58('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',true)&input=VHpSYVZVTlZNbFJOUlRSSVFUWk1TRkJHV2tkVE5WcFRTelZaVlUxWlNsbElRazVFUjAwelJFZEtUa2hCVlRKV1NrSkhWa05XTWxsUFJsVkZTek15UkU5R1RVVk5Na05hUjBZMVJVMVZVbHBOVWxOSFMxSlNXRTlDUTFWVlUxcFpTazR5U0VGV1ZGVlBWVEpHUXpKRFYwMDBXbFV5VVZOSFNscEJWRk5OVVQwPQ)