from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import subprocess




bg_color = (0, 0, 0, 180)
fg_color = (255, 255, 0)
img1 = Image.open('img2.png')
blur_1 = img1.filter(ImageFilter.GaussianBlur(1))
enhancer = ImageEnhance.Brightness(blur_1)
blur_2 = enhancer.enhance(1.1)

mytmp = blur_2.copy()
mytmp.save('tmp.png', dpi=(50,50))

process = subprocess.Popen(['./i_c_u', 'img1.png', 'tmp.png'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = process.communicate()
out = out.decode()
print(out)
out_lines = out.split('\n')
dist = int(out_lines[2].split(':')[1])
