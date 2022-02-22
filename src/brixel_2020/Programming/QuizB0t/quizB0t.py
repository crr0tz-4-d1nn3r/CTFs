# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 21:19:46 2021

"""

from selenium import webdriver
from time import sleep

chromedriver = '../../chromedriver.exe'

url = 'http://timesink.be/quizbot/index.php'

Q_A = {}
count = 0

question_xpath = '/html/body/div[2]/h4'
ans_xpath = r'//*[@id="answer"]'
txtBox_xpath = r'//*[@id="insert_answer"]'

ansBtn_xpath = r'/html/body/div[2]/form/input[2]' # no feedback at top
ansBtn_incorrect_xpath = r'/html/body/div[4]/form/input[2]' # incorrect answer
ansBtn_correct_xpath = r'/html/body/div[3]/form/input[2]' # correct

# open first instance of browser. 
d1 = webdriver.Chrome(chromedriver)
d1.get(url)

# open another instance of browser
d2 = webdriver.Chrome(chromedriver)
d2.get(url)

# use the first instance to get the answer by pressing the 
# answer button and reading the response
d1.find_element_by_xpath(ansBtn_xpath).click()
ans = d1.find_element_by_xpath(ans_xpath).text
sleep(0.5)

# use the second instance to submit the answer and get the credit
d2.find_element_by_xpath(txtBox_xpath).send_keys(ans)
d2.find_element_by_xpath(ansBtn_xpath).click()
sleep(0.5)

while count < 1000:
    count += 1   
  
    # use the first instance to get the answer by pressing the 
    # answer button and reading the response
    d1.find_element_by_xpath(ansBtn_incorrect_xpath).click()
    ans = d1.find_element_by_xpath(ans_xpath).text
    sleep(0.5)
    
    # use the second instance to submit the answer and get the credit
    d2.find_element_by_xpath(txtBox_xpath).send_keys(ans)
    d2.find_element_by_xpath(ansBtn_correct_xpath).click()
    sleep(0.5)

