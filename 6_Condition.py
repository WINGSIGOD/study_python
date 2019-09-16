# coding=utf-8
# Python Conditional statements


''':if statements'''
flag = False
name = "luren"
if name == "python":
    flag = True
else:
    print name

''' elif statements'''
num = 5
if num == 3:
    print "boss"
elif num == 2:
    print "user"
elif num == 1:
    print "worker"
else:
    print "roadman"

'''if语句多个条件'''
num = 9
if num >= 0 and num <= 10:
    print "hello"
num = 10
if num < 0 or num > 10:
    print "hello"
else:
    print "undefine"

num = 8
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print "hello"
else:
    print "undefine"

var = 100
if (var == 100): print "ver = 100"
print "good bye!"
