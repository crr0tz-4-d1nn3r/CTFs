from scapy.all import *
import re

a = rdpcap('capture .pcap')
sessions = a.sessions()
i = 1
for session in sessions:
    http_payload = ""
    for packet in sessions[session]:
        char = str(packet)[-12]
        print(char, end='')

