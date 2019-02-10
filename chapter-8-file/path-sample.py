#! python3
# -*- coding:utf-8 -*-
import sys,os,time,logging
# 其实win7/win10的系统下，已经不需要分区D:\了，不是吗？只C:\一个分区即可。
pathName = os.path.join('C:\\Users\y00300912','Documents','FeedbackHub')
print('pathname(windows):'+pathName)

pathName = os.path.join('usr','bin','yzchaogmail')
print('pathname(Linux):'+pathName)
current_dir = os.getcwd()
print('current dir:'+current_dir)
os.chdir('c:\\windows\\')
print(os.getcwd())
os.chdir(current_dir)
if not os.path.exists('.\\dir-1\\dir-2\\dir-3'):
    os.makedirs('.\\dir-1\\dir-2\\dir-3')
else:
    print("'path exists: '.\\dir-1\\dir-2\\dir-3'")
    # print(str(err))
print('current dir:'+os.getcwd())
if not os.path.exists('.\\dir4'):
    os.mkdir('.\\dir4')
else:
    print("mkdir: .\\dir4 exist.")
print('abspath:' + os.path.abspath(sys.argv[0]))
print('isabs:' + str(os.path.isabs(sys.argv[0])))
print('relpath:'+os.path.relpath('d:\\',sys.argv[0]))
print('basename:' + os.path.basename(sys.argv[0]))
print('dirname:' + os.path.dirname(sys.argv[0]))
print('path.split():'+ str(os.path.split(sys.argv[0])))
print('pathsize:'+str(os.path.getsize((sys.argv[0]))))

print('listdir:',end='')
print(os.listdir(os.getcwd()))

print(os.path.exists('c:\\windows\\'))
print(os.path.isfile('c:\\windows\system32\\'))
print(os.path.isdir('c:\\windows'))
