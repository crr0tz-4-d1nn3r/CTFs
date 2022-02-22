# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 19:30:48 2021

"""
from selenium import webdriver

# where is the driver
chromedriver = 'chromedriver.exe'

# url to visit
url = 'http://timesink.be/speedy/'

# xpath of elements to interact with
rndStr_xpath = r'//*[@id="rndstring"]'
input_xpath = r'//*[@id="inputfield"]'
submit_xpath = r'//*[@id="submitbutton"]'

# start the driver
driver = webdriver.Chrome(chromedriver)

# visit the page
driver.get(url)

# get the string
rndstr = driver.find_element_by_xpath(rndStr_xpath).text

# input string into input box
driver.find_element_by_xpath(input_xpath).send_keys(rndstr)

# click enter
driver.find_element_by_xpath(submit_xpath).click()

# brixelCTF{sp33d_d3m0n}