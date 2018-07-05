#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

'''
问题二：数值比较
n = [9,15,23,89,33,26,2,76]
请编写代码，找出数组中的最大数与最小数
'''

def cmp(s):
    max,min = 0,0
    for i in range(len(s)):
        if s[i] > s[max]:
            max = i
        elif s[i] < s[min]:
            min = i
    print 'max is %s, min is %s' %(s[max], s[min])

if __name__ == '__main__':
    s = [9,15,23,89,33,26,2,76]
    cmp(s)
