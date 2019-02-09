#! python3
# -*- coding:utf-8 -*-
import pprint
dictSample={}

dictSample.setdefault('key1',{})
dictSample['key1'].setdefault('key2',{})
dictSample['key1']['key2'].setdefault('key3','value')

print(dictSample)
pprint.pprint(dictSample)
