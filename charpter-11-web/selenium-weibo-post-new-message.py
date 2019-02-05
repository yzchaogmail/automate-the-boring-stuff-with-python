#! python3
#! Selenium Webdriver元素定位的八种常用方式
#! https://www.cnblogs.com/qingchunjun/p/4208159.html
############################################################
import os,requests,time,sys
from selenium import webdriver

if len(sys.argv)<2:
    print("Usage : PYTHON-FILE Password")
    exit()
else:
    password_text = sys.argv[1]

options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values' :
        {
        'notifications' : 2
         }
}
options.add_experimental_option('prefs',prefs)
#driver = webdriver.Chrome(chrome_options = options)

url =  'http://weibo.com'
try:
    browser = webdriver.Chrome(chrome_options = options)
    browser.get(url)
except:
    print('Cannot open "webo.com"')
    exit()
time.sleep(8)

try:
    loginname = browser.find_element_by_id('loginname')
    loginname.send_keys('amthe')
except:
    print('Faild to find loginname')
    exit()
try:
    #password = browser.find_element_by_class_name('password')
    password = browser.find_element_by_name('password')
    password.send_keys(password_text)
except:
    print('Failed to find password')
    exit()

#Login weibo.com
try:
    #loginButton = browser.find_element_by_tag_name('登录')
    #loginButton = browser.find_element_by_partial_link_text("登录")
    loginButton = browser.find_element_by_class_name("login_btn")
    loginButton.click()
except:
    print('Failed to find LoginButton')
    exit()
time.sleep(1)

try:
    inputContent = browser.find_element_by_tag_name("textarea")
    inputContent.send_keys('Selenium Sample about login weibo and post new message')
except:
    print('Failed to find element "textarea" ')
    exit()

try:
    postWeibo = browser.find_element_by_class_name('W_btn_a')
    postWeibo.click()
except:
    print('Failed to find element "postWeibo"')
