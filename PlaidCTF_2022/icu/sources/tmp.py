from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import subprocess

def make_img(w, h, text, bg_color, fg_color):
    img = Image.new('RGBA',(w,h), bg_color)
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf" , 50)
    d.text((10,10), text, font=fnt, fill=fg_color)
    return img


bg_color = (0, 0, 0, 75)
fg_color = (255, 255, 0)
img2 =  make_img(500, 90, 'give me the flag', bg_color, fg_color)
img2.thumbnail(( 250,70))

img1 = Image.open('img1.png')
blur_1 = img1.filter(ImageFilter.GaussianBlur(12))
enhancer = ImageEnhance.Brightness(blur_1)
blur_2 = enhancer.enhance(0.8)

mytmp = blur_2.copy()
mytmp.paste(img2, (60, 135), img2)
mytmp.save('tmp.png', dpi=(50,50))

process = subprocess.Popen(['./i_c_u', 'img1.png', 'tmp.png'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = process.communicate()
out = out.decode()
print(out)
out_lines = out.split('\n')
dist = int(out_lines[2].split(':')[1])
