# RTX CTF 2021 Finals
 Held Sep 10 - 21 for RTX employees that made it through the first round of challenges and are currently eligible to compete in the finals. The finals consist of several categories that will test a broad range of CyberSecurity, Development, and Problem Solving skills. The challenges vary from being simple puzzles all the way up to practical exploitation.

# TOC
| Catagory | Name | Description |
|:---|---|---|
| Network | [Merriam-Webster](Network/Merriam_Webster/) | Hydra dictionary attck on SSH weak password |
| Network | [Cute Problems](Network/CuteProblems) |File upload and Apport exploits |
| Network | Organized Questions | |
| Network | Even we were shocked | |
| Network | RmluZCB0aGUgU2hhcmU= | |
| Crypto | [Their Office](Crypto/01_Their_Office/) | Aircrack-ng WPA passphrase recovery |
| Crypto | [Encrypted File](Crypto/02_Encrypted_File/) | XOR encoded and password protected archive |
| Crypto | [Layers](Crypto/03_Layers/) | OpenSSL 1.1 and password protected archive |
| Crypto | Hash Service | |
| Crypto | The Rosenberg | |
| Forensics | [The Office](Forensics/01_The_Office/) | Message hidden in the metadata of image|
| Forensics | [Even Pugs See It](Forensics/02_Even_Pugs_See_It/) | Message hidden in signle color plane of the image|
| Forensics | [Archive Matryoshka](Forensics/03_Archive_Matryoshka/) | Esoteric archive nesting doll |
| Forensics | [04_USB_Drive](Forensics/04_USB_Drive/)| Plain-text attack on archive|
| Forensics | Beep Beep | |
| Misc | Lets Adventure | |
| Misc | Bootloader | |
| Binary/RE | [Log-in](Rev/01_Log_In/) | Buffer overflow |
| Binary/RE | Backup | |
| Binary/RE | Sessions | |
| Binary/RE | [Time Traveler](Rev/04_Time_Travler/) | XOR Time-y thing |
| Binary/RE | Secure SRAM | |
| Misc | Lets Adventure | |
| Misc | Bootloader | |
| Web | Mysterious C2 Web service | |

# Tool Reference
A quick breakdown of the tools used while solving these challenges.

## Forensics
- [https://www.wireshark.org/](https://www.wireshark.org/)
- [https://www.aircrack-ng.org/](https://www.aircrack-ng.org/)
- [https://github.com/danielmiessler/SecLists/tree/master/Passwords](https://github.com/danielmiessler/SecLists/tree/master/Passwords)
- [https://wimlib.net/](https://wimlib.net/)
- [https://sourceforge.net/projects/kgbarchiver/](https://sourceforge.net/projects/kgbarchiver/)
- [https://www.elcomsoft.com/archpr.html](https://www.elcomsoft.com/archpr.html)
- https://github.com/vanhauser-thc/thc-hydra
- [http://oldhome.schmorp.de/marc/fcrackzip.html](http://oldhome.schmorp.de/marc/fcrackzip.html)


## RE
- [https://ghidra-sre.org/](https://ghidra-sre.org/)
- [https://rada.re/n/](https://rada.re/n/)
- [https://gist.github.com/williballenthin/6857590dab3e2a6559d7](https://gist.github.com/williballenthin/6857590dab3e2a6559d7)

## Stego
- [https://exiftool.org/](https://exiftool.org/)
- [https://github.com/zardus/ctf-tools/blob/master/stegsolve/install](https://github.com/zardus/ctf-tools/blob/master/stegsolve/install)
