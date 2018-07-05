#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

'''
# 使用 while 循环打印 1 3 5 7 9
'''

def odd(end):
    i = 1
    while i<=end:
        yield i
        i=i+2

if __name__ == '__main__':
    for i in odd(9):
        print i
