# https://docs.wand-py.org/en/0.6.3/guide/install.html#install-imagemagick-on-windows
# https://www.geeksforgeeks.org/wand-swirl-function-in-python/

# Import Image from wand.image module 
from wand.image import Image 
  
# Read image using Image function 
with Image(filename ='kiddie_pool.png') as img: 
  
    # swirl image using swirl() function 
    img.swirl(degree =-900) 
    img.save(filename ="unpool.png") 