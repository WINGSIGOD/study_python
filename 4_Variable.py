#coding=utf-8
#变量类型

#对象赋值
counter = 100 #赋值整形变量
miles = 1000.0 #浮点型
name = "wiku"#字符串
print counter
print miles
print name

#同时赋值 赋值相同
a=b=c=1
print a,b,c

#同时赋值 赋值不同
a,b,c=1,2.0,"bobo"
print a,b,c

'''
Python有五个标准的数据类型：
Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）
'''

var1 = 1
var2 = 10
del var2
print var1#,var2
#输出:name 'var2' is not defined 只会输出var1的值

#字符串
'''
左到右0→∞
右到左-∞←0
'''
s = 'abcdefg'
print s[1:5]

#字符串各种使用
str = '1234567890'
print str
print str[0]
print str[1:5]
print str[2:]
print str * 2
print str + "TEST"
print str[:-1]
print str[-6:-2]

#列表 列表可以无元素[]
list = ['runoob',123,3.123,'happe',"hello world",9.87]
tinylist = [123]
tinylist1 = []
print list
print list[0]
print list[1:3]
print list[2:]
print tinylist * 3
print list+tinylist
print list+tinylist+tinylist1

#元组 元素必须多个元素()
tuple = ('runoob',123,4.56,'john',710.23)
tinytuple = (5550,2220)
print  tuple
print tuple[0]
print tuple[1:3]
print tuple[2:]
print tinytuple*3
print tuple + tinytuple

#元组内元素不允许更新和修改 列表可以
tuple = ('runoob',789,2.23,'john',72.2)
list = ['runoob',789,2.23,'john',72.2]
#tuple[2] = 1000
#'tuple' object does not support item assignment报错
#表示元组不能修改
list[2] = 1000

#字典{} 注意保序
dict = {}
dict['one'] = "This is one"
dict['2']="This is two"
tinydict={'name':'john','code':1234,'dept':'sales'}
print dict['one']
print dict['2']
print tinydict
print tinydict.keys()
print tinydict.values()
