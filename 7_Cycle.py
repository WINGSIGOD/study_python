# coding=utf-8
# Python cycle statements

print "while cycle"
'''while cycle'''

count = 0
while (count < 9):
    print "the count is:", count
    count += 1
print "good bye"

'''Contiune and break instructions'''
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print i
    break

i = 1
while 1:
    print i
    i += 1
    if i > 10:
        break

'''Unlimited cycle'''
var = 1
while var == 1:
    num = raw_input("Enter a number :")
    print "you entered:", num
    print "goodbye"
    break  # if you want to try unlimited cycle,you can try to comment this line

'''Use else statement in cycle'''
count = 0
while count < 5:
    print  count, "is less than 5"
    count += 1
else:
    print count, "is not less than 5 "

'''
flag=1
while(flag):print "given flag is really true!"
print  "good bye"
'''
