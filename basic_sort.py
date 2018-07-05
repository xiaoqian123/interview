#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

'''
问题一：字符串排序
s = "hello world"
请编写代码，将 s 以 [a-z] 顺序输出
'''

def sort(s):
    tmp = list(s.replace(' ', ''))
    for i in range(len(tmp)-1):
        for j in range(i):
            if tmp[i] > tmp[j+1]:
                tmp[i],tmp[j+1] = tmp[j+1],tmp[i]
    return ''.join(tmp)

if __name__ == '__main__':
    s = "hello world"
    print sort(s)
    

