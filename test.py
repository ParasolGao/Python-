# -*- coding: utf-8 -*-
def trim(s):
    start = 0
    end = 0
    for index,val in enumerate(s,1):
        if(val != ' '):
            start = val
    for index,val in enumerate(s,-1):
        if(val != ' '):
            print(s[index])
s = '   hello  '
trim(s)