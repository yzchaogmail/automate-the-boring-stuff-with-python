#! python3
import os,requests,bs4

url = 'http://Xkcd.com'
os.makedirs('xkcd',exist_ok = True)

while not url.endswith('#'):
    #TODO:Download the page
    print('Navigatoring pages: %s' %url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,"html5lib")

    #TODO:Find the url of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find "comic img"')
    else:
        imgUrl = comicElem[0].get('src')
        print('Dowinloading image:%s' %imgUrl)
    #TODO:Download the image
        imageContext = requests.get('http:' + imgUrl)
        imageContext.raise_for_status()
    #TODO:Save the image to ./xkcd/
        fileName = os.path.join('xkcd',os.path.basename(imgUrl))
        try:
            fileSave = open(fileName,"wb")
            print('Save image as:%s' %fileName)
        except:
            print('Open file failed:%s' %fileName)

        for chunk in imageContext.iter_content(10000):
            fileSave.write(chunk)
        fileSave.close()

    #TODO:Get the prev button's url
    urlPrev = soup.select('a[rel="prev"]')[0]
    url = 'http://Xkcd.com' + urlPrev.get('href')

print('Done.')
