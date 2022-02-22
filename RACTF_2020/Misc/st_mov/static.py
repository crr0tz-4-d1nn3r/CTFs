"""
raCTF 020
ST.MOV
youtube link: https://youtu.be/HkIJRzzHP5E
ractf{video time bois}
"""
import cv2
from glob import glob


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

# Main 
if __name__ == '__main__':
    # used VLC to download video from youtube
    movie = 'videoplayback.mp4'
    
    # determine if a frame represents a 1 (static)
    # or a 0 (no static)
    bstr = getDataFromMovie(movie)
    
    # opencv seems to have trouble with the very first frame
    # assume the first frame is the same as the next
    bstr = bstr[0] + bstr[0:]
    
    # something is broken with this challenge
    # we get 2280 frames, which at 30 fps is 76 sec = correct time
    # If we assume 15 frames per bit, thats 152 bits.
    # at 7 bits per character, that's 21.714285 characters?
    # there seems to be two bits missing. That's 30 frames,
    # or 1 sec of data. Youtube compression? challenge error?
    # here's the hack, for this challenge, based on knowing the flag
    # if you have 5 0's in a row, add one more, 
    # 6 places to the left - seriously wtf?
    c = 0
    bflag = ''
    while c < len(bstr):
        bflag += bstr[c]
        if sum([int(x) for x in bflag[-5:]]) == 0:
            bflag = bflag[:-6] + '0' + bflag[-6:]
        c += 15
    
    c = 0
    flag = ''
    tmp = ''
    while c < len(bflag):    
        tmp = '0'+ bflag[c:c+7]
        flag += chr(int(tmp,2))
        c += 7
    print(flag)