# Browsing Websites
50 pts

Browse to http://10.174.12.14/

author: @NOPResearcher

## Flag
```
ts{TheFirstTunnelIsTheEasiest}
```

## Solution
```
python3
import requests
requests.get('http://10.174.12.14').content
```

Gets the content of the page. On it is the flag.