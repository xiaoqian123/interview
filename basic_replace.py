#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import
import re

'''
问题三：替换
a = "i,am,a,student,in,chengdu"
请编写代码，将 “student” 和 “chengdu” 变为可基于参数输入配置的输出
通过参数输入打印出完整的句子
'''

def check(a,oldStr,newStr):
    if oldStr in a and newStr in a:
        return True
    else:
        return False

def rep(a,oldStr,newStr):
    s = re.split(',', a)
    for i in range(len(s)):
        if oldStr == s[i]:
            s[i] = newStr
    return ','.join(s)

if __name__ == '__main__':
    a = "i,am,a,student,in,chengdu"
    if check(a,'student','chengdu'):
        print rep(a,'student','chengdu')
    else:
        print 'substr is Not exist'
