from selenium import webdriver
import sys
from selenium.webdriver.common.keys import Keys

if len(sys.argv) < 2:
    print('Usage selenium-facebook-login.py PASSWORD')
    exit()
else:
    password = sys.argv[1]
    #print('Password = %s' %(password))

browser = webdriver.Chrome()
browser.get('http://www.facebook.com')

try:
    elemEmail = browser.find_element_by_id('email')
    elemEmail.send_keys('yzchao@gmail.com')
except:
    print('Failed to find Email element.')
    exit()

try:
    elemPass = browser.find_element_by_id('pass')
    elemPass.send_keys(password)
except:
    print('Failed to find Pass element')
    exit()
try:
    elemLogin = browser.find_element_by_id('loginbutton')
    elemLogin.click()
except:
    print('Failed to find loginbutton')
    exit()

try:
    elemHtml = browser.find_element_by_tag_name('html')
    elemHtml.send_keys(Keys.END)
    elemHtml.send_keys(Keys.HOME)
except:
    print('Failed to get tag HTML')

'''


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