#!/usr/bin/env python

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The Numbers"

for num in numbers:
    print num

def iterate(num,inc):
    x = 0
    y = []
    while x < num:
        y.append(x)
        x += inc
    return y


my_num = int(raw_input("Give me a number :> "))
my_inc = int(raw_input("Give me an incriment :> "))

print iterate(my_num,my_inc)

for b in range(0,100,10):
    print b

