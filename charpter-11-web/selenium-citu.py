from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('http://citu-ai.huawei.com')

try:
    elements = browser.find_elements_by_class_name('ivu-input')
except:
    print('Failed find_elements_by_class_name ivu-input')
    exit()

count = 0
for elem in elements:
    if count == 0:
        elem.send_keys('z00408803')
        time.sleep(1)
    elif count == 1:
        elem.send_keys('password-need-to-change')
        time.sleep(1)
    else:
        break;
    count+=1

try:
    elemIvuLogin = browser.find_element_by_class_name('ivu-btn')
except:
    print('Failed find_element_by_class_name(ivu-btn)')
    exit()

elemIvuLogin.click()
exit()