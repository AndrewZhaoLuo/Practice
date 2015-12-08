# -*- coding: utf-8 -*-
'''
The hyperexponentiation or tetration of a number a by a positive integer b,
denoted by a↑↑b or ba, is recursively defined by:

a↑↑1 = a,
a↑↑(k+1) = a(a↑↑k).

Thus we have e.g. 3↑↑2 = 33 = 27, hence 3↑↑3 = 327 = 7625597484987 and
3↑↑4 is roughly 103.6383346400240996*10^12.

Find the last 8 digits of 1777↑↑1855.
'''

DIGITS_NEEDED = 8
BASE = 1777
EXPONENT = 1855

#defined as n↑↑p
#only keeps tracks of the last digits as denoted by DIGITS_NEEDED
def hyperExpo(n, p):
    return n

#step 1: find the parity of 1777, how many times will I need to multiply 1777 before
#I get the last DIGITS_NEEDED digits again?

#index, 0 = 000... 0, 12 = 000... 12, etc. up to DIGITS_NEEDED digits
digitsReached = [False] * (10 ** DIGITS_NEEDED)
prod = 1
multiplyCount = 0
while not digitsReached[prod]:
    digitsReached[prod] = True
    multiplyCount += 1
    prod *= BASE
    prod = prod % (10 ** DIGITS_NEEDED)

print "Need: " + str(multiplyCount) + " multiplications to repeat last " + str(DIGITS_NEEDED) + " digits"
    
