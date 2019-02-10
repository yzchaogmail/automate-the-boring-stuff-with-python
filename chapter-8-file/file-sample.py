#! python3
# -*- coding:utf-8 -*-
import sys,os,time,logging

filename = None
fileContent = None
try:
    filename = open('hellox.txt','r')
except Exception as err:
    print('failed to open file:'+str(err))

if None != filename:
    try:
        fileContent = filename.read()
    except Exception as err:
        print('failed to readfile:'+str(err))
else:
    print('None of filename')

if None != fileContent:
    print(fileContent)

filename = None
fileContent = None

try:
    filename = open(sys.argv[0])
except Exception as err:
    print('failed to open file:'+str(err))

if None != filename:
    try:
        fileContent = filename.readlines()
        filename.close()
    except Exception as err:
        print('failed to readlines:'+str(err))
else:
    print('None of filename')

if None != fileContent:
    fileWrite = open('fileToWrite.txt','w')
    for linesContent in fileContent:
        fileWrite.write(linesContent)
    fileWrite.close()
else:
    print('Nothing to write.END')

#
# lineContent = filename.readline()
# while None != lineContent:
#     print(lineContent)
#     lineContent = filename.readline()
#
