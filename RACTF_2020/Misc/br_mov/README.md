# BR.MOV
400 points

https://youtu.be/zi3pLOaUUXs

## References and Tools
Open CV - https://pypi.org/project/opencv-python/

VLC Player Download Youtube Videos -
https://lifehacker.com/the-best-hidden-features-of-vlc-1654434241

Pyzbar - https://pypi.org/project/pyzbar/

## Flag
```shell
ractf{b4rc0d3_m4dn3ss}
```

## Solution
Much easier than ST.MOV. Decoding does not depending on frame rate, and it appears that no data was missing from this challenge. Some frames did not decode well. I decided to dump all the frames and deal with issues as I came across them. Warning - I made each frame into an image. If you run this code, make sure to have a folder ready for the images. Alternativly, rewrite the code to decode each frame as it's grabbed and don't store the images.

Download the movie and work locally. This function will extract the frames and save them:

```python
def extractImages(pathIn, pathOut):
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
      success,image = vidcap.read()
      if success:
          cv2.imwrite( pathOut + "frame%03d.jpg" % count, image)
      count += 1
```

Decode each image:
```python
def decode(im) : 
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)
    msg = ''
    if decodedObjects != []:       
            msg = decodedObjects[0].data.decode()

    return msg
```

The first character is the index into the barcode data where the character of the flag is. It is also the value that is spoken if you listen to the video. With that, you have the flag.
```python
chrArr = []
for m in data:
    chrArr.append(m[int(m[0])])

flag = ''.join([x for x in chrArr])
print(flag)
```
