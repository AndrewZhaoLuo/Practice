# -*- coding: utf-8 -*-
'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

#cocatenating 1,2,3,4,5,6,7,8,9,10...

MAX_DIGITS  = 1000000
totalDigits = 0
num         = 1
ds          = [] #index 0 = d1, index 1 = d10, etc.

total       = 1 #answer to the question

while MAX_DIGITS > totalDigits:
    #find the number of the digits in current num
    tempNum     = num
    digitCount  = 1
    while tempNum > 9:
        digitCount += 1
        tempNum /= 10
    
    #figure out if we managed to get past a digit of interest
    for i in xrange(7):
        if totalDigits < 10 ** i and totalDigits + digitCount >= 10 ** i:
            #extract the relevant digit
            tempNum = num
            digitIndex = totalDigits + digitCount - 10 ** i
            while digitIndex > 0:
                tempNum /= 10
                digitIndex -= 1
            ds.append(tempNum % 10)

    #updadte digit count
    totalDigits += digitCount
    num += 1

print ds
