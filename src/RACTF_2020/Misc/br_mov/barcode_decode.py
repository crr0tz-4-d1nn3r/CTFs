"""
raCTF Sun Jun  7 21:15:57 2020
BR.MOV
youtube link: https://youtu.be/zi3pLOaUUXs
ractf{b4rc0d3_m4dn3ss}
"""
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
from glob import glob
import sys
import argparse


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

def decode(im) : 
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)
    msg = ''
    if decodedObjects != []:       
            msg = decodedObjects[0].data.decode()

    return msg


# Main 
if __name__ == '__main__':
    
    # used VLC to download video from youtube
    movie = 'videoplayback.mp4'
    pathOut = ''
    
    # WARNING!!!
    # extract images to same folder as this script is running
    extractImages(movie, pathOut)
    
    # grab all the extracted images in the folder
    files = glob('*.jpg')
    data = ['']
    for file in files:
        im = cv2.imread(file)
        msg = decode(im)
        # there are duplicate frames and some that don't decode well
        if msg != '' and msg != data[-1]:
            data.append(msg)
        
    # remove init data
    data = data[1:]
    
    # the first character is the index into the barcode data where
    # the character of the flag is
    chrArr = []
    for m in data:
        chrArr.append(m[int(m[0])])
    
    flag = ''.join([x for x in chrArr])
    print(flag)