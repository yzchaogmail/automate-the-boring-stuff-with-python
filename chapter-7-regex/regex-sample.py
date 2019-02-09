#! python3
# -*- coding:utf-8 -*-
#  ?匹配零次或一次前面的分组。
#  *匹配零次或多次前面的分组。
#  +匹配一次或多次前面的分组。
#  {n}匹配n 次前面的分组。
#  {n,}匹配n 次或更多前面的分组。
#  {,m}匹配零次到m 次前面的分组。
#  {n,m}匹配至少n 次、至多m 次前面的分组。
#  {n,m}?或*?或+?对前面的分组进行非贪心匹配。
#  ^spam 意味着字符串必须以spam 开始。
#  spam$意味着字符串必须以spam 结束。
#  .匹配所有字符，换行符除外。
#  \d、\w 和\s 分别匹配数字、单词和空格。
#  \D、\W 和\S 分别匹配出数字、单词和空格外的所有字符。
#  [abc]匹配方括号内的任意字符（诸如a、b 或c）。
#  [^abc]匹配不在方括号内的任意字符。


import re
import logging
logging.basicConfig(filename='debugfile.txt',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')

#about basic Regex.compile,search//
logging.debug('basic example----->:')
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My Number is 415-555-3232.')
logging.debug('phone number found:%s' %mo.group())

#about {} and (),groups,group(1),group(2)
logging.debug('About "()" example----->:')
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search('My another phone number is 444-111-5698')
#logging.debug('phone number found:%s' %mo.group)
logging.debug(mo.groups())
logging.debug('group:%s,group[1]:%s,group[2]:%s' %(mo.group(),mo.group(1),mo.group(2)))

#About | example
logging.debug('About "|" example----->:')
heroRegex = re.compile(r'Batman|Tina Fey')
mo = heroRegex.search('Batman and Tina Fey')
logging.debug(mo.group())
mo = heroRegex.search('Tina Fey and Batman')
logging.debug(mo.group())

#about  ? 0/1 times
logging.debug('\nAbout "?" example----->:')
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
logging.debug(mo.group())

mo = batRegex.search('The Adventures of Batwoman')
logging.debug(mo.group())
#   ? another example
phoneRegex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mo = phoneRegex.search('My others number1: 415-555-4242')
logging.debug(mo.group())

mo = phoneRegex.search('My others number1: 555-4242')
logging.debug(mo.group())

#about   * 0-n times example:
logging.debug('\nAbout "*" example----->:')
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batwowowowowowowoman')
logging.debug('about 7 times match:%s' %mo.group())
mo = batRegex.search('The Adventures of Batman')
logging.debug('NO time match:%s' %mo.group())

#about   + 1-n times example:
logging.debug('\nAbout "+" example----->:')
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batwowowowowowowoman')
logging.debug('about 7 times match:%s' %mo.group())
mo = batRegex.search('The Adventures of Batman')
if(None == mo):
    logging.debug('+ Patton match None')
else:
    logging.debug('+ Patton Match:%s' %(mo.group()))

#about charcator class:\d,\D,\w,\W,\s,\S
logging.debug('\nAbout "\d\s\w" example------>:')
xmaxRegex = re.compile(r'\d+\s\w+')
moList = xmaxRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
logging.debug(moList)
# for i in range(1,len(moList)+1):
#     logging.debug('"\d\s\w Match[%d]:%s"' %(i,moList[i-1]))

#about [My Patten]
logging.debug('\nAbout my patten[]:')
constantRegex = re.compile(r'[aeiouAEIOU]')
mo = constantRegex.findall('RoboCop eats baby food. BABY FOOD.')
logging.debug(mo)
# for i in range(len(mo)+1):
#     logging.debug(mo[i])
logging.debug('\nAbout my patten[^]:')
constantRegex = re.compile(r'[^aeiouAEIOU]')
mo = constantRegex.findall('RoboCop eats baby food. BABY FOOD.')
logging.debug(mo)

#about ^$ Patten
logging.debug('\nAbout ^$ patten:')
beginWith = re.compile(r'^Hello')
mo = beginWith.findall('Hello world! Here is Georgeyang Speaking.')
logging.debug(mo)
mo = beginWith.findall('Here is Georgeyang Speaking.')
logging.debug(mo)

endWith = re.compile(r'world$')
mo = endWith.findall('Hello world! Here is Georgeyang Speaking.')
logging.debug(mo)
mo = endWith.findall('Here is Georgeyang Speaking.Hello world')
logging.debug(mo)

wholeNumber = re.compile(r'^\d+$',re.DOTALL)
mo = wholeNumber.findall('12356672041840581450')
logging.debug(mo)
mo = wholeNumber.findall('''abc12356672041840581450\n
123456088888\n
14314123''')
logging.debug(mo)
mo = wholeNumber.findall('12356672041840581450xyz')
logging.debug(mo)

#About . patten:match any charactor:
logging.debug('\nAbout . patten:------>')
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
logging.debug(mo)

atRegex = re.compile(r'<.*>')
mo = atRegex.findall('search(<To serve man> for dinner.>')
logging.debug(mo)

atRegex = re.compile(r'<.*?>')
mo = atRegex.findall('search(<To serve man> for dinner.>')
logging.debug(mo)

atRegex = re.compile(r'<.*>',re.DOTALL)
mo = atRegex.findall('search(<To serve man> for dinner.>\nsearch(<To serve man> for dinner.>\nsearch(<To serve man> for dinner.>')
logging.debug(mo)

#about ignorecase:re.IGNORECADE|re.I
ignorecaseRegex = re.compile(r'ignoreCASE',re.IGNORECASE)
mo = ignorecaseRegex.findall('ignoreCASE,IGNORECASE,ignorecase,IGNOREcase')
logging.debug(mo)

#about sub() :replace()
nameRegex = re.compile(r'Agent \w+')
mo = nameRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob.')
logging.debug(mo)

nameRegex = re.compile(r'Agent (\w)\w*')
mo = nameRegex.sub(r'\1******','Agent Alice gave the secret documents to Agent Bob.')
logging.debug(mo)

#about complict express
logging.debug('\nAbout complict express example:------->')
expRegex = re.compile(r'''(
                    (\d{3}|\(\d{3}\))?          # area code,0 or 1
                    (\s|-|\.)?                  # seperate of area code
                    \d{3}                       #
                    (\s|-|\.)                   # seperate of area code
                    \d{4}                       #
                    (\s*(ext|x|ext.)\s*\d{2,5})?
                    )''',re.VERBOSE)
mo = expRegex.findall('abcd 333-4444 020-444-5555 (020)-111-2222e1234')
logging.debug(mo)
