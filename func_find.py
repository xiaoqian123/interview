#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

'''
# 编写一个函数，查找数字 6 是否在列表 l 里，如果在，输出“found”，如果不在，输出“not found”
l = [1,5,7,8,9]
'''

def find(numList,findNum):
    isfind = False
    for i in range(len(numList)):
        if findNum == numList[i]:
            isfind = True
            break

    if isfind:
        print "found"
    else:
        print "not found"

if __name__ == '__main__':
    l = [1,5,7,8,9]
    find(l,6)
