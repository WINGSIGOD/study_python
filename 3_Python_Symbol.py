# coding=utf-8
# This file involved many symbols,debug with breakpoints

# Python line break symbol
print "hello";
print "runoob";

'''
#python标识符
and;        exec;       not;
assert;     finally;    or;
break;      for;        pass;
class;      from;       print;
continue;   global;     raise;
def;        if;         return;
del;        import;     try;
elif;       in;         while;
else;       is;         with;
except;     lambda;     yield;
'''

# Python indentation
if True:
    print "True"
else:
    print "False"

'''
#缩进错误示范
if True:
    print "Answer"
    print "True"
else:
    print "Answer"
    #下面这行缩进错误,会报错,需要注释掉
  print "False"
    #IndentationError: unindent does not match any outer indentation level
    # 错误表明:
    # 你使用的缩进方式不一致，有的是 tab 键缩进，有的是空格缩进，改为一致即可。
    # IndentationError: unexpected indent错误
    # 是在告诉你"Hi，老兄，你的文件里格式不对了，可能是tab和空格没对齐的问题"
    # 所有 python 对格式要求非常严格。
'''

# Multi-line connector
print "total = item_one " \
      "item_two " \
      "item_three"

# Multi-line connector by objest thinking
total = 'item_one' + \
        'item_two' + \
        'item_three'

print total

# [], {} or () uesd for multi-line connector
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print days

# use of ''
'''
''用于词语
'''
print 'hello'

'''
"""用于段落
包含多行语句"""
'''
print """hello
the
world"""

'''
注释方式:
#单行注释
''' '''多行注释
'''

# Waiting for user input, just a function
raw_input("按下 enter 退出,其他任意按键显示....\n")

# The method is to write str to stream output. It will not default to the last line break.
import sys;

x = 'runoob';
sys.stdout.write(x + '\n')

x = "a"
y = "b"
# Line feed output
print x
print y

print '--------------------'
# No line feed output 1
print x,
print y,

# No line feed output 2
print x, y
