# The Office
100

We found this image inspecting access logs from a compromised system, we think the attackers have hidden some data inside of it. Can you find it?

[RTX-Stego-lvl1.zip](RTX-Stego-lvl1.zip)

# Flag
```
RTXFLAG{Dwight_was_Right}
```

# Solution
The archive has a jpg. Looking at metatdata.
```$ exiftool False.jpg 
ExifTool Version Number         : 11.88
File Name                       : False.jpg
Directory                       : .
File Size                       : 35 kB
File Modification Date/Time     : 2021:05:10 23:07:36-05:00
File Access Date/Time           : 2021:09:10 11:47:05-05:00
File Inode Change Date/Time     : 2021:09:10 11:47:05-05:00
File Permissions                : rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Exif Byte Order                 : Big-endian (Motorola, MM)
XP Comment                      : 525458464C41477B4477696768745F7761735F52696768747D
Padding                         : (Binary data 1864 bytes, use -b option to extract)
Image Width                     : 450
Image Height                    : 311
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 450x311
Megapixels                      : 0.140
```

The XP Comment seems sus. Decoding as ASCII
```
$ echo 525458464C41477B4477696768745F7761735F52696768747D | xxd -r -p
RTXFLAG{Dwight_was_Right}
```

# Reference
- [https://exiftool.org/](https://exiftool.org/)