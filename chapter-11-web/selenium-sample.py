from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
#type(browser)
browser.get('http://www.sina.com')

try:
    elemHtml = browser.find_element_by_tag_name('html')
    elemHtml.send_keys(Keys.END)
    time.sleep(3)
    elemHtml.send_keys(Keys.HOME)
except:
    print('Failed to find tag HTML')
    exit()




'''
try:
    elemEmail = browser.find_element_by_id('email')
    elemEmail.send_keys('yzchao@gmail.com')
except:
    print('Failed to find Email element.')
    exit()

try:
    elemPass = browser.find_element_by_id('pass')
    elemPass.send_keys('//')
except:
    print('Failed to find Pass element')
    exit()
try:
    elemLogin = browser.find_element_by_id('loginbutton')
    elemLogin.click()
except:
    print('Failed to find loginbutton')

#about invent-with-python
browser.get('http://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('card-block')
    print('Found <%s> element with that class name!' %(elem.tag_name))
except:
    print('Was not able to find an element with that name.')

try:
    elem = browser.find_element_by_link_text('Read Online for Free')
    type(elem)
    elem.click();
except:
    print('Failed to find element by link text .')
'''