#! python3
# -*- coding=utf-8 -*-
#   reise Exception()
#   traceback.format_exc()
#   try/except Exception as err
#   assert()
#   logging.debuging()
#   IDLE(GO/Step/Over/Quit/BreakPoint)

import logging,traceback
import random

logging.basicConfig(filename='debuglog.txt',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')

logging.disable(logging.CRITICAL)
def exceptionSample():
    raise Exception("Error for exception sample.")
def successSample():
    print('Success for run funciton')

try:
    exceptionSample()
    logging.info('success to try exceptionSample')
except Exception as err:
    logging.debug('Exception sample:%s',str(err))
    logging.debug(traceback.format_exc())

# # python debug-sample.py -O or ignore assert()
# assert(1==0)
# # python debug-sample.py -O or ignore assert()

heads = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads = heads + 1
    if i == 500:
        print('Halfway done!')
print('Heads came up ' + str(heads) + ' times.')
