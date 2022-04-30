from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import subprocess


def add_overlay_box(in_file, box_size, i, d):
    
    with Image.open(in_file) as img:
        h,w = img.size
        step_h = h//16
        step_w = w//16
        x =  loc % w
        y =  loc % h
        new_img = Image.new('RGBA',(box_size, box_size), color)
        img.paste(new_img, (x, y), new_img)
        img.save(in_file,dpi=(70,70))


def check_hash(img1_file, img2_file):
    process = subprocess.Popen(['./i_c_u', img1_file, img2_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    out = out.decode()
    #print(out)
    out_lines = out.split('\n')
    hash1 = out_lines[0].split(':')[1]
    hash2 = out_lines[1].split(':')[1]
    dist = int(out_lines[2].split(':')[1])
    texted = out_lines[4].split(':')[1]
    return hash1, hash2, dist, texted

def strDif(a, b):
    inds = [i-1 for i in range(len(a)) if a[i] != b[i]]
    difs = [ord(a[i])-ord(b[i]) for i in inds]
    return inds, difs

img1_file = 'img1.png'
img2_file = 'tmp.png'
img3_file = 'img3.png'
subprocess.Popen(['cp', 'tmp.png', 'img3.png'])
hash1, hash2, dist, texted = check_hash(img1_file, img2_file)
loc = 200
box_size  = 16
while dist != 0:
    print(f' Image1 hash: {hash1}\n Image2 hash: {hash2}\n Hamming Distance: {dist}\n Image 2 text: {texted}')
    if dist < 4:
        color = (255, 255, 255, 150)
    else:
        color = (10, 10, 10, 150)

    inds, difs = strDif(hash1, hash2)
    print(inds)
    print(difs)
    
    i = inds[0]
    d = difs[0]

    add_overlay_box(img3_file, box_size, i, d)
        
    hash1, hash2, dist, texted = check_hash(img1_file, img3_file)






