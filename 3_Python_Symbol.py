#coding=utf-8
#python标识符学习
#本文件涉及多个标识符 建议断点测试

#python换行符
print "hello";print "runoob";


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

#python缩进
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

#多行连接符
print "total = item_one " \
      "item_two " \
      "item_three"

#也是多行连接符 但是使用对象思维
total = 'item_one' + \
        'item_two' + \
        'item_three'

print total

# [], {} 或 () 括号多行连接,使用对象思维
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print days

#引号的使用
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

#等待用户输入,只是个函数,只有退出功能,留一行给用户舒服而已
raw_input("按下 enter 退出,其他任意按键显示....\n")

#该方法是将str写入流方式输出.不会默认最后换行
import sys;
x = 'runoob';
sys.stdout.write(x + '\n')

x="a"
y="b"
#换行输出
print x
print y

print '--------------------'
#不换行输出方法1
print x,
print y,

#不换行输出方法2
print x,y


