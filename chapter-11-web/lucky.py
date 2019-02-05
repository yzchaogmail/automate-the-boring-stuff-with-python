#!python3
import sys,webbrowser,requests,bs4

print(sys.version)
res = requests.get('http://www.google.com/search?q='+ ' '.join(sys.argv[1:]))
res.raise_for_status()

'''
tempFile = open("googleSearch.html","wb")
for chunk in res.iter_content(100000):
    tempFile.write(chunk)
tempFile.close()
'''

bsContent = bs4.BeautifulSoup(res.text,"html5lib")
elements = bsContent.select('.r a')

count = min(5,len(elements))
for i in range(count):
    webbrowser.open('http://google.com'+elements[i].get('href'))
