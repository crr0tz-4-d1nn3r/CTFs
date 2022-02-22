# ST.MOV
250 points

https://youtu.be/HkIJRzzHP5E

## References and Tools
Open CV - https://pypi.org/project/opencv-python/

VLC Player Download Youtube Videos - https://lifehacker.com/the-best-hidden-features-of-vlc-1654434241

## Flag
```shell
ractf{video time bois}
```

## Solution
Something seems broken with this challenge. We get 2280 frames, which at 30 fps is 76 sec = correct time. If we assume 15 frames per bit, thats 152 bits. At 7 bits per character (Ascii printable characters only need 7 bits), that's 21.714285 characters? There seems to be 2 bits missingin the middle of the message. That's 30 frames, or 1 sec of data. Youtube compression? Frame rate loss? Challenge error? Here's the hack, for this challenge, based on guessing the flag.  If you have 5 0's in a row, add one more, 6 places to the left. Seriously wtf?

Download the movie, this code works locally. This function decodes the frames, 0 for black/tone, 1 for static
```python
def getDataFromMovie(movie):
    vidcap = cv2.VideoCapture(movie)
    success,image = vidcap.read()
    count = 0
    bstr = ''
    success = True
    
    while success:
      success,image = vidcap.read()
      if success:
          # if a pixle is black, record a 0
          # if static, record 1
          if image[0,0,0]<10:
              bstr += '0'
          else:
              bstr += '1'
    return bstr;
```

I've noticed that opencv has trouble grabbing the first frame. I interpolate that frame as being the same as the next one. 
```python
bstr = bstr[0] + bstr[0:]
```

Other than that first frame, I didn't notice any others getting skipped. Assume 15 frames per bit and the missing 2 bits, decode the frame array from step 2.
```python
    c = 0
    bflag = ''
    while c < len(bstr):
        bflag += bstr[c]
        if sum([int(x) for x in bflag[-5:]]) == 0:
            bflag = bflag[:-6] + '0' + bflag[-6:]
        c += 15
```

Decode binary string to ascii characters:
```python
    c = 0
    flag = ''
    tmp = ''
    while c < len(bflag):    
        tmp = '0'+ bflag[c:c+7]
        flag += chr(int(tmp,2))
        c += 7
    print(flag)
```