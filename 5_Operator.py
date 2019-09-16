# coding=utf-8
# Python Operator

print "算数运算符"

'''
#算数运算符
a=10，b=20
+   加 - 两个对象相加  a + b 输出结果 30
-   减 - 得到负数或是一个数减去另一个数 a - b 输出结果 -10
*   乘 - 两个数相乘或是返回一个被重复若干次的字符串   a * b 输出结果 200
/   除 - x除以y    b / a 输出结果 2
%   取模 - 返回除法的余数    b % a 输出结果 0
**  幂 - 返回x的y次幂 a**b 为10的20次方， 输出结果 100000000000000000000
//  取整除 - 返回商的整数部分（向下取整）
如
9//2=4
-9//2=-5
'''

a = 21
b = 10
c = 0
print "a=", a
print "b=", b
print "c=", c

c = a + b
print "c为a,b的和", c

c = a - b
print "c为a,b的差", c

c = a * b
print "c为a,b的积", c

c = a / b
print "c为a,b的商", c

c = a % b
print "c为a,b的余", c

# 修改a,b
print "修改a,b"
print "a=", a
print "b=", b
a = 2
b = 3
print "a=", a
print "b=", b

c = a ** b
print "c为a,b的幂", c
c = a // b
print "c为a,b的商 向下取整", c

a = 10
b = 5
print "a=", a
print "b=", b
c = a // b
print "c为a,b的商 向下取整", c

print "-" * 20

print "比较运算符"
'''
#比较运算符
所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价
==  等于 - 比较对象是否相等                (a == b) 返回 False。
!=  不等于 - 比较两个对象是否不相等          (a != b) 返回 true.
<>  不等于 - 比较两个对象是否不相等          (a <> b) 返回 true。这个运算符类似 != 。
>   大于 - 返回x是否大于y                  (a > b) 返回 False。
<   小于 - 返回x是否小于y。                 (a < b) 返回 true。
>=  大于等于 - 返回x是否大于等于y。          (a >= b) 返回 False。
<=  小于等于 - 返回x是否小于等于y。          (a <= b) 返回 true。
'''

a = 21
b = 10
c = 0

print "a=", a
print "b=", b
print "c=", c

if a == b:
    print "a=b"
else:
    print "a<>b"

if a != b:
    print "a<>b"
else:
    print "a=b"

if a <> b:
    print "a<>b"
else:
    print "a=b"

if a < b:
    print "a<b"
else:
    print "a>=b"

if a > b:
    print "a>b"
else:
    print "a<=b"

a = 5
b = 20
print "修改a,b"
print "a=", a
print "b=", b
if a <= b:
    print "a<=b"
else:
    print "a>b"

if b >= a:
    print "b>=a"
else:
    print "a<b"

print "-" * 20

print "赋值运算符"
'''
=   简单的赋值运算符    c = a + b 将 a + b 的运算结果赋值为 c
+=  加法赋值运算符     c += a 等效于 c = c + a
-=  减法赋值运算符     c -= a 等效于 c = c - a
*=  乘法赋值运算符     c *= a 等效于 c = c * a
/=  除法赋值运算符     c /= a 等效于 c = c / a
%=  取模赋值运算符     c %= a 等效于 c = c % a
**= 幂赋值运算符       c **= a 等效于 c = c ** a
//= 取整除赋值运算符    c //= a 等效于 c = c // a
'''

a = 21
b = 10
c = 0

print "a=", a
print "b=", b
print "c=", c
c = a + b
print "c=", c

c += a
print "c += a 等效于 c = c + a c=", c

c /= a
print "c /= a 等效于 c = c / a c=", c

c = 2
print "c=", c
c %= a
print "c %= a 等效于 c = c % a c=", c

c **= a
print " c **= a 等效于 c = c ** a c=", c

c //= a
print "c //= a 等效于 c = c // a c=", c

print "-" * 20

print "数位运算符"

'''
数位运算时先把树变成二进制再变为十进制来运算 运算过程为二进制 输出结果为10进制
a = 0011 1100
b = 0000 1101
-----------------
a&b = 0000 1100
a|b = 0011 1101
a^b = 0011 0001
~a  = 1100 0011

&   按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
|   按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
^   按位异或运算符：当两对应的二进位相异时，结果为1
~   按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。~x 类似于 -x-1
<<  左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0
>>  右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数
'''

a = 60
print "a=60 = 0011 1100"
b = 13
print "b=13 = 0000 1101 "
c = 0

c = a & b;
print "c=a&b", c, "12 = 0000 1100"

c = a | b;
print "c=a|b", c, "61 = 0011 1101"

c = ~a;
print "c=~a", c, "49 = 0011 0001"

c = a << 2
print "c=a<<2", c, "240 = 1111 0000"

c = a >> 2
print "c=a>>2", c, "15 = 0000 1111"

print "-" * 20

print "逻辑运算符"

'''
and x and y 布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。
or  x or y  布尔"或" - 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。
not not x   布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。
'''

a = 10
b = 20
print "a=", a
print "b=", b
if a and b:
    print "a and b are true"
else:
    print "a or b are false"

if a or b:
    print "a or b are true"
else:
    print "a and b are flalse"

a = 0
print "a=", a
if a and b:
    print "a and b are true"
else:
    print "a or b are false"

if a or b:
    print "a or b are true"
else:
    print "a and b are false"

if not (a and b):
    print "a or b is false"
else:
    print "a and b is true"

print "-" * 20

print "成员运算符"
'''
in      如果在指定的序列中找到值返回 True，否则返回 False。
not in  如果在指定的序列中没有找到值返回 True，否则返回 False。
'''
a = 10  # type: int
b = 20
list = [1, 2, 3, 4, 5];
print "a=", a
print "b=", b
print "list=", list
if (a in list):
    print "a in list"
else:
    print "a not in list"

if (b not in list):
    print "b not in list"
else:
    print "b in list"

a = 2
print "modify a=", a

if (a in list):
    print "a in list"
else:
    "a not in list"

print "-" * 20
print "成员运算符" \
 \
      '''
      is      is 是判断两个标识符是不是引用自一个对象
      is not  is not 是判断两个标识符是不是引用自不同对象
      '''
a = 20
b = 20
print "a=", a
print "b=", b

if (a is b):
    print "a and b have same id"
else:
    print "a and b have not same id"

if (a is not b):
    print "a and b have not same id"
else:
    print "a and b have same id"

b = 30
print "motify b=", b

if (a is b):
    print "a and b have same id"
else:
    print "a and b have not same id"

if (a is not b):
    print "a and b have not same id"
else:
    print "a and b have same id"

'''
is 与 == 区别：
is 用于判断两个变量引用对象是否为同一个(同一块内存空间)
== 用于判断引用变量的值是否相等。
'''

print "-" * 20
'''
Python运算符优先级
**                          指数 (最高优先级)
~ + -                       按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //                    乘，除，取模和取整除
+ -                         加法减法
>> <<                       右移，左移运算符
&                           位 'AND'
^ |                         位运算符
<= < > >=                   比较运算符
<> == !=                    等于运算符
= %= /= //= -= += *= **=    赋值运算符
is is not                   身份运算符
in not in                   成员运算符
not and or                  逻辑运算符
'''

a = 20
b = 10
c = 15
d = 5
e = 0
print "a=", a
print "b=", b
print "c=", c
print "d=", d
print "e=", e

e = (a + b) * c / d
print "e=(a+b)*c/d=", e

e = ((a + b) * c) / d
print "e=(a+b)*c/d=", e

e = a + (b * c) / d
print "e=(a+b)*c/d=", e
