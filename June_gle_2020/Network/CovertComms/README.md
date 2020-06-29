README

# Covert Comms
50 points

Can you find the flag?

## flag:
```shell
flag{How_did_you_find_this}
```

## Solution
Download pcap file, open in wire shark. The packet data contaings one characher that is changing. If you step through the traffic, you can start getting a feel for what's going on.

Time for python. I'm using scapy (https://scapy.net/) to open and parse the pcap. Then I just print the character of interest to the console:
```python
from scapy.all import *

a = rdpcap('capture .pcap')
sessions = a.sessions()
i = 1
for session in sessions:
    http_payload = ""
    for packet in sessions[session]:
        char = str(packet)[-12]
        print(char, end='')
```

The result is:
```shell
There's ot to be a flag in here somewhere, I know there are covert comms, I just need to find the flag}siht_dnif_uoy_did_woH{galfseriously, somehere in here some where, I hope I'm not doing this manually......
```

They hid the flag backwards.

