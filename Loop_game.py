# -*- coding: UTF-8 -*-

# Guess the size
import random

s = int(random.uniform(1, 10))
# print(s)
m = int(input('输入整数:'))
while m != s:
    if m > s:
        print('大了')
        m = int(input('输入整数:'))
    if m < s:
        print('小了')
        m = int(input('输入整数:'))
    if m == s:
        print('OK')
        break;

'''
#mora
# -*- coding: UTF-8 -*-

import random
while 1:
    s = int(random.randint(1, 3))
    if s == 1:
        ind = "石头"
    elif s == 2:
        ind = "剪子"
    elif s == 3:
        ind = "布"
    m = raw_input('输入 石头、剪子、布,输入"end"结束游戏:')
    blist = ['石头', "剪子", "布"]
    if (m not in blist) and (m != 'end'):
        print "输入错误，请重新输入！"
    elif (m not in blist) and (m == 'end'):
        print "\n游戏退出中..."
        break
    elif m == ind :
        print "电脑出了： " + ind + "，平局！"
    elif (m == '石头' and ind =='剪子') or (m == '剪子' and ind =='布') or (m == '布' and ind =='石头'):
        print "电脑出了： " + ind +"，你赢了！"
    elif (m == '石头' and ind =='布') or (m == '剪子' and ind =='石头') or (m == '布' and ind =='剪子'):
        print "电脑出了： " + ind +"，你输了！"
'''
'''
#Shake the dice
# -*- coding: utf-8 -*-

import random
import sys
import time

result = []
while True:
    result.append(int(random.uniform(1,7)))
    result.append(int(random.uniform(1,7)))
    result.append(int(random.uniform(1,7)))
    print result
    count = 0
    index = 2
    pointStr = ""
    while index >= 0:
        currPoint = result[index]
        count += currPoint
        index -= 1
        pointStr += " "
        pointStr += str(currPoint)
    if count <= 11:
        sys.stdout.write(pointStr + " -> " + "小" + "\n")
        time.sleep( 1 )   # 睡眠一秒
    else:
        sys.stdout.write(pointStr + " -> " + "大" + "\n")
        time.sleep( 1 )   # 睡眠一秒
    result = []
'''

'''
#Decimal to binary
# -*- coding: UTF-8 -*-

denum = input("输入十进制数:")
print denum,"(10)",
binnum = []
# 二进制数
while denum > 0:
    binnum.append(str(denum % 2)) # 栈压入
    denum //= 2
print '= ',
while len(binnum)>0:
    import sys
    sys.stdout.write(binnum.pop()) # 无空格输出print ' (2)'
'''

'''
#九九乘法表
# -*- coding: UTF-8 -*-

i = 1
while i:
    j = 1
    while j:
        print j, "*", i, " = ", i * j, '  ',
        if i == j:
            break

        j += 1
        if j >= 10:
            break

    print "\n"
    i += 1
    if i >= 10:
        break
'''
