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

total       = 1 #answer to the question

while MAX_DIGITS > totalDigits:
    #find the number of the digits in current num
    tempNum     = num
    digitCount  = 0
    while tempNum > 0:
        digitCount += 1
        tempNum /= 10
    num += 1
    
    totalDigits += digitCount

