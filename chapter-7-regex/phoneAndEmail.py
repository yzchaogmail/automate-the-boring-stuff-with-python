#! python3
# -*- coding:utf-8 -*-

import re,sys,os,time,pyperclip

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
  )''',re.VERBOSE)

# moPhone = phoneRegex.search('(123)-123-1234 x 12345')
# print(moPhone[1],moPhone[2],moPhone[3],moPhone[4],moPhone[5],moPhone[6],moPhone[7],moPhone[8],moPhone[9])

emailRegex = re.compile(r'''(
    ([\w\d.%+-_])+
    (@)
    (\w)+
    (\.)
    (\w{2,4})
)''',re.VERBOSE)

# mo = emailRegex.search('geroge.yang@huawei.com abcd_xyz@gmail.com')
# print(mo)
text = pyperclip.paste()
moPhoneList = phoneRegex.findall(text)
moEmailList = emailRegex.findall(text)

matches = []
for groups in moPhoneList:
    if('' == groups[1]):
        phoneNum = '-'.join([groups[3], groups[5]])
    else:
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[7] != '':
        phoneNum += ' x ' + groups[8]
    matches.append(phoneNum)
    # matches.append(groups[0])     #会有一些空格、ext、ext.等对不齐的问题
for groups in moEmailList:
    matches.append(groups[0])

# print(matches)

if len(matches)>0:
    for i in matches:
        print(i)
else:
    print('Null phone-number and email-address match.')
