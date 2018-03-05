# -*- coding: utf-8 -*-
def trim(s):
    for index,value in enumerate(s):
        if(value != ' '):
            start = index
            break
    for index,value in enumerate(range(len(s),-1,1)):
        if(value != ' '):
            end = index
            break
    for idx in range(s[start+1],start[end],1)

# 测试:
if trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')