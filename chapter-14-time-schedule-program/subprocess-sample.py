#! python3
# -*- coding:utf-8 -*-

import os,sys,logging
import subprocess as sp

#sp.Popen(['notepad.exe','hello.txt'])
logging.basicConfig(filename='debuglog.txt',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')

sp.Popen('notepad.exe')
sp.Popen(['notepad.exe','temp.txt'])

logging.debug('before----------------')
sp.Popen(['start','start-hell0.txt'],shell=True)
logging.debug('after----------------')
