#  Their Office
100

While sitting outside of the building of the attackers in our hack back operation, we found a network broadcasting there was only one in the area so we assume it was theirs... can you do anything with this? We would like to be able to connect to their network but it's passworded and we don't know the password.

NOTE: This challenge is one where the RTXFLAG{} is not required, the data you obtain IS the flag, there is no other data needed submit what you find as the flag. Make sure to pay careful attention to the last sentence in the challenge description.

NOTE2:* The crypto category mostly 'involves' cryptography for challenges but doesn't necessary fall in line with what you'd see in most cryptography challenges in other CTFs, this is just a heads-up... there are at least 1 or 2 that fall in line with it but hopefully this sets expectations.

[capture-01.pcap](capture-01.pcap)

# Flag
```
aeiou123@
```

# Solution
Opened file in Wireshark. Definatly a Wifi capture. Turned to Aircrack-ng to see if any handshakes in the capture.
```
$ aircrack-ng capture-01.pcap
 #  BSSID              ESSID                     Encryption

   1  00:3A:9A:E6:75:07  test lab                  WPA (1 handshake, with PMKID)
```

Now to see if we can crack the passphrase. Started with good ol' Rockyou.txt wordlist and got a hit.

```
$ aircrack-ng capture-01.pcap -w rockyou.tx
Reading packets, please wait...
Opening capture-01.pcap
Read 1719 packets.

   #  BSSID              ESSID                     Encryption

   1  00:3A:9A:E6:75:07  test lab                  WPA (1 handshake, with PMKID)

Choosing first network as target.

Reading packets, please wait...
Opening capture-01.pcap
Read 1719 packets.

1 potential targets



                               Aircrack-ng 1.6 

      [00:16:04] 10186303/14344391 keys tested (10731.70 k/s) 

      Time left: 6 minutes, 27 seconds                          71.01%

                           KEY FOUND! [ aeiou123@ ]


      Master Key     : 3F 42 0B 04 EA DF 84 85 FF 6A 5D 61 9B EE AE 02 
                       A6 FE 49 C1 BD 3A 41 FE D8 DC 68 FB E6 A8 6F 58 

      Transient Key  : 22 77 1F 4D 94 CA AA F5 46 D8 9A CA F6 3F 33 73 
                       85 3C CB 2C EC 11 3F 64 F7 D0 D7 9D 5B E8 47 80 
                       33 EB 4D E6 1A C8 04 0C 73 8E E9 57 0B DE 66 00 
                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 

      EAPOL HMAC     : 79 F1 53 30 6A DA A0 DD 11 4F 19 F8 01 43 5B C6
```

## References
- [https://www.wireshark.org/](https://www.wireshark.org/)
- [https://www.aircrack-ng.org/](https://www.aircrack-ng.org/)
- [https://github.com/danielmiessler/SecLists/tree/master/Passwords](https://github.com/danielmiessler/SecLists/tree/master/Passwords)