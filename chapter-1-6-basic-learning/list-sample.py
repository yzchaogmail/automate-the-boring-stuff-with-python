#! python3
# -*- coding:utf-8 -*-
listsample = ['abc','qwe',234,'wetb']
for i in range(len(listsample)):
    print(listsample[i])
listsample.append('AppendEND')
for item in listsample:
    print(item)

listsample.insert(0,'InsertHead')
print(listsample)
print(listsample.index(234))

tupleSample = tuple(listsample)
print(tupleSample)
print('index of qwe='+ str(tupleSample.index('qwe')))
