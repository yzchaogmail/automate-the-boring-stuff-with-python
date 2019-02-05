import requests

try:
    res = requests.get('https://www.ietf.org/rfc/rfc2328.txt')
    res.raise_for_status()
except:
    print('Failed to get URL')
    exit(-1)
'''
print(type(res))
print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text[:1024])
'''
try:
    filewrite = open('rfc2328.txt','wb')
except:
    print('Failed to open write file rfc2328.txt: ')

for chunk in res.iter_content(100000):
    filewrite.write(chunk)

filewrite.close()
