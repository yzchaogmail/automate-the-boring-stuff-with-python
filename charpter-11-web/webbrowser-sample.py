import webbrowser,sys,pyperclip
import requests
if len(sys.argv) > 1:
    address = ' '.join(sys.artv[1:])
else:
    address = pyperclip.paste()
webbrowser.open('http://www.google.com/maps/place/' + address )