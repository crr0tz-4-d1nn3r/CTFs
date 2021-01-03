import pyzbar.pyzbar as pyzbar
import cv2
import numpy as np
from selenium import webdriver
from time import sleep
import requests
import base64


#file = 'qr-code.png'
#file = 'barcode.png'
file='barcode2.png'

# chrome Driver location
chromedriver = r'chromedriver.exe'

# provided file
file = 'qr-code.png'
im = cv2.imread(file)


# Find barcodes and QR codes
decodedObjects = pyzbar.decode(im)
msg = ''
if decodedObjects != []:       
        url = decodedObjects[0].data.decode()

print(url)


# website has a barcode, which when decoded, and output submitted takes you to 
# another page ... this prompted this route.
img_xpath = '/html/body/div/img'
txtbx_xpath = '/html/body/div/form/input[1]'
submit_xpath = '/html/body/div/form/input[2]'

driver = webdriver.Chrome(chromedriver)
driver.get(url)
sleep(1)    

count = 1
while True:
    file = 'barcode' + str(count) + '.png'
    try:
        driver.find_element_by_xpath(img_xpath).screenshot(file)
    except:
        break
     
    im = cv2.imread(file)
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)
    msg = ''
    if decodedObjects != []:       
            msg = decodedObjects[0].data.decode()
    

    if msg == '':
        break # the last one is not decoded by this library - use another online app
        
    print(msg)
    
    driver.find_element_by_xpath(txtbx_xpath).send_keys(msg)
    driver.find_element_by_xpath(submit_xpath).click()
    sleep(1)
    count += 1

# output of qr-code.png
# http://www.timesink.be/qrcode/flag.html
# code-128-easy
# 5449000133335
