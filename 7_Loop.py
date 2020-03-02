# coding=utf-8
# Python Loop statements

print "while Loop"
'''while Loop'''

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

'''Unlimited Loop'''
var = 1
while var == 1:
    num = raw_input("Enter a number :")
    print "you entered:", num
    print "goodbye"
    break  # if you want to try unlimited Loop,you can try to comment this line

'''Use else statement in Loop'''
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


print "for Loop"
'''for Loop'''

for letter in "python":
    print "current letter",letter

fruits=['banana','apple','mango']
for fruit in fruits:
    print "current fruit:",fruit
print "goodbye"

fruits=['banana','apple','mango']
for index in range(len(fruits)):
    print "current fruit:",fruits[index]
print "goodbye"

'''Loop through the else statement'''
for num in range(10,20):
    for i in range(2,num):
        if num%i==0:
            j=num%i
            print "%d equal %d*%d"%(num,i,j)
            break
    else:
        print num,"is a prime number"