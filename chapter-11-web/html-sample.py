import requests
import webbrowser
from selenium import webdriver
#browser = webbrowser.open('www.github.com')

browser = webdriver.Chrome()
browser.get('https://github.com/login')