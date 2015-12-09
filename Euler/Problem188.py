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

'''
From the googology wiki:
the last digits of x↑↑y converge as y -> infinity.
The last d digits of x↑↑y in base b can be defined by:

N(0) = x
N(d + 1) = x^N(d) % 10 ^ d in base 10.

as y gets bigger. derived from the euler phi function
'''

'''
last digits converge as y gets bigger (credit googlepedia). Idea then is
to leverage built in pow function with fast modulus to win
'''
remainder = 1
for i in xrange(1, EXPONENT + 1):
    remainder = pow(BASE, remainder, 10 ** DIGITS_NEEDED)

print remainder
'''
OLD SOLUTION BELOW
#defined as n↑↑p
#only keeps tracks of the last digits as given
def hyperExpo(n, p, parity, digits):
    if p == 1:
        return n % (10 ** digits)

    #remainder left is the remaining exponent we must evaluate
    #% parity prevents overflows
    remainder = (n ** n) % (parity)
    return hyperExpo(remainder, p - 1, parity, digits)

def getMultiplicativeParity(base,  digits):
    digitsReached = [False] * (10 ** digits)
    prod = base
    multiplyCount = 1
    while not digitsReached[prod]:
        digitsReached[prod] = True
        multiplyCount += 1
        prod *= base
        prod = prod % (10 ** digits)

    return multiplyCount

#step 1: find the parity of 1777, how many times will I need to multiply 1777 before
#I get the last DIGITS_NEEDED digits again?

#index, 0 = 000... 0, 12 = 000... 12, etc. up to DIGITS_NEEDED digits
#print "Need: " + str(getMultiplicativeParity(BASE, DIGITS_NEEDED)) + " multiplications to repeat last " + str(DIGITS_NEEDED) + " digits"
    
print hyperExpo(3, 3, getMultiplicativeParity(3,8), 8)


'''
