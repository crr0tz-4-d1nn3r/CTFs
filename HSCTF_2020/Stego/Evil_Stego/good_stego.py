import random
from PIL import Image
from typing import List, Tuple

filename = 'orig.png'

with Image.open(filename) as image:
    image = image.convert("RGB")
    pixels = image.load()
    available = image.width * image.height * 3
    valid_spots = []
    for channel in range(3):
        for y in range(image.height):
            for x in range(image.width):
                valid_spots.append((x, y, channel))

    # grab the metadata which sould be 60 bytes located in the first 60 * 8 = 480 locations
    metadata = ''
    for i in range(480):
        x, y, channel = valid_spots[i]
        orig = list(pixels[x, y])
        metadata += str(orig[channel] & 1)
        
    # figure out what the seed was, and the length of the message
    a = int(metadata[-64:-56], 2)  
    b = int(metadata[-56:-48], 2)  
    c = int(metadata[-48:-40], 2)  
    d = int(metadata[-40:-32], 2)           
    size = int(metadata[-32:-24], 2)
    seed = [a,b,c,d]
    
    # determine locations and order of data
    random.seed(bytes(seed))
    locations = random.sample(valid_spots[480:], size * 8 + 1)    
    
    # get the binary flag
    msg = ''
    for loc in locations:
        x, y, channel = loc
        orig = list(pixels[x, y])
        msg += str(orig[channel] & 1)
    
    # convert binary to ascii
    flag = ''
    for i in range(0, len(msg), 8):
        flag += chr(int(msg[i:i + 8], 2))
    print(flag)