README

# DoS Level 1-1
10 points

Who is the target of the UDP Flood DOS?

DOS_1.pcap
## flag
```shell
23.110.211.178
```

## solution
Download pcap, open in Wireshark. Filter on UDP traffic. The destination of all that traffic is the flag.


# DoS Level 1-2
10 points

What destination port was used DOS?

DOS_1.pcap

## flag
```shell
2821
```

## solution
Same pcap as before. Filter on UDP traffic. From destination in prior challenge, look at the port being used.


# DoS Level 1-3
10 points

What ASN does the target of the UDP Flood DOS belong to?

DOS_1.pcap

## flag
```shell
AS395954
```

## solution
Same pcap as before. Filter on UDP traffic. Wasn't sure what ASN was, but it came up earlier in Discord:
```
[11:28 AM] Pl4gue: what is ASN ? in networking
[11:28 AM] Pl4gue: full form of asn ?
[11:29 AM] pwneip: it's take just the number or as#####
[11:30 AM] Pl4gue: hmmm
[11:31 AM] Pl4gue: im really confused
[11:32 AM] RaralMirlo: it is autonomous system number used for BGP
[11:32 AM] Pl4gue: aaah okey
```

https://hackertarget.com/wireshark-tutorial-and-cheat-sheet/

Shows how to look for this in the pcap. but It looked blank in mine. so I used  https://www.ultratools.com/tools/asnInfo to get 
```shell
AS395954
Country: US
Registration Date: 2017-02-02
Registrar: arin
Owner: LEASEWEB-USA-LAX-11, US
```

Went with that first value: AS395954


# DoS Level 2-1
10 points

How many different types of DNS record queries in total were made during the attack?

DOS_2.pcap

## flag
```shell
4
```

## solution
Download and open the pcap for this challenge. All traffic is DNS queries, so don't need to filter. Note the the "type" of query is listed in the data

![36bc1d7c860c5ffab65dcc0167e9280e.png](../../../../_resources/3adeed71ca614efe8149ebb33fc3f911.png)

Apply that field as a column and sort. From there we see that there are 4 types of queries: *, A, AAAA, and PTR



# DoS Level 2-2
10 points

What domain was being requested during the DNS DoS attack?

DOS_2.pcap

## flag
```shell
1rip.com
```

## solution
Same pcap from prior challenge. Most of the queries are of type A. Those are looking for 1rip.com.



# DoS Level 3-1
10 points

What IP is the "attacker" in this scenario?

DOS_3.pcap

## flag
```shell
172.16.0.22
```

## solution
New pcap. There are two ip's , pick one. 50% chance right?
