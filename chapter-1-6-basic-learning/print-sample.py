#! python3
# -*- coding:utf-8 -*-
listx=['a','b','c','d']
print('-'.join(listx))
print('list1='+listx[0]+',list2='+listx[1]+',list3='+listx[2])
for i in range(len(listx)):
    print(listx[i],end=' ',sep='-')
print('\n')
print(listx[0],listx[1],listx[2],sep='-',end='')
print('++++++++')
