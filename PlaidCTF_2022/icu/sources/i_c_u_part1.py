from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import subprocess
from base64 import b64decode

def make_part1_img(outfile, hashstr, text_to_match):
    target = [bin(x)[2:].rjust(8, '0') for x in b64decode(hashstr)]
    img = Image.new('L', (9, 8), 255)

    for row in range(8):
        for col in range(9):
            x = 8 - col
            y = row
            if col == 0:
                continue
            prev = img.getpixel((x + 1, y))
            if target[row][col - 1] == '1':
                cur = prev - 1
            else:
                cur = 255
            img.putpixel((x, y), cur)
    
    
    img = img.resize((1000, 1000), Image.NEAREST)

    # add text
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf" , 12)
    d.text((0, 0), text_to_match, font=fnt, fill=200)
    img.save(outfile, dpi=(70,70))


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


# files to start with
img1_file = 'img1.png'
img2_file = 'img2.png'
img3_file = 'part1.png'
text_to_match = 'give me the flag'

# check hash - won't be good, but gives us a start
hash1, hash2, dist, texted = check_hash(img1_file, img2_file)
print(f' Image1 hash: {hash1}\n Image2 hash: {hash2}\n Hamming Distance: {dist}\n Image 2 text: {texted}')

# make part 1 image
make_part1_img(img3_file, hash1, text_to_match)

# check
hash1, hash2, dist, texted = check_hash(img1_file, img3_file)
print(f' Image1 hash: {hash1}\n Image2 hash: {hash2}\n Hamming Distance: {dist}\n Image 2 text: {texted}')






