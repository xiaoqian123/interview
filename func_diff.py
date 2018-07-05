#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

'''
# 将字符串 s 拆分成两个字符串 s1、s2，其中 s1 只包含字母，转换为小写，以 [a-z] 排序，s2 只包含数值，升序排序
s = "aAsnr3id2d4b6gs7DZsf9e1AF"

解题思路：
先进行字母转换，在进行排序，在进行拆分
'''

'''转换函数'''
def Atoa(sList):
    for i in range(len(sList)):
        tmp = ord(sList[i])
        if tmp >= 65 and tmp <= 90:
            sList[i]=chr(ord(sList[i])+32)
    return sList

'''排序'''
def sort(aList):
    for i in range(len(aList)-1):
        for j in range(i,len(aList)-1):
            if aList[i] > aList[j+1]:
                aList[i],aList[j+1] = aList[j+1],aList[i]
    return aList

def diff(s):
    sList = list(s) 
    aList = Atoa(sList)
    orderList = sort(aList) 
    newStr = ''.join(orderList)

    for i in range(len(orderList)):
        if ord(newStr[i]) > 57: 
            break

    numStr = newStr[0:i]
    lStr = newStr[i:]
    return [numStr, lStr]

if __name__ == '__main__':
    s = "aAsnr3id2d4b6gs7DZsf9e1AF"
    [numStr, lStr]=diff(s)
    print numStr,lStr

