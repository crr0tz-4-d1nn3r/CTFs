from PIL import Image, ImageDraw, ImageFont
import base64
import subprocess
from time import sleep
import random

def make_img(w, h, text, bg_color, fg_color):
    img = Image.new('RGBA',(w,h), bg_color)
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf" , 80)
    d.text((10,10), text, font=fnt, fill=fg_color)
    
    return img

def add_noise(img, n):
    w, h = img.size
    pixels = img.load()

    for i in range(n):
        x = random.randint(0,w-1)
        y = random.randint(0,h-1)
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        pixels[x,y] = (r,g,b, 255)

    return img


def add_lines(img, n):
    w, h = img.size
    pixels = img.load()
    for i in range(n):
        for j in range(w):
            pixels[j,h-n+i] = (255,255,255, 255)
    return img


img =  make_img(500, 400, '\n give  me\n\n the flag', (250, 175, 200), (0,0,0))

for i in range(0, 5000):
    img = add_noise(img, i)
    img.save('tmp.png', dpi=(70,70))

    with open('img1.png','rb') as f:
        img1_b64 = base64.b64encode(f.read())


    with open('tmp.png','rb') as f:
        img2_b64 = base64.b64encode(f.read())

    process = subprocess.Popen(['./i_c_u', 'img1.png', 'tmp.png'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    out = out.decode()
    print(out)
    out_lines = out.split('\n')
    dist = int(out_lines[2].split(':')[1])
    if dist == 0:
        break
    sleep(0.1)