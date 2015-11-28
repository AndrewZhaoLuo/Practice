# -*- coding: utf-8 -*-
'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first
Fibonacci number for which the last nine digits are 1-9 pandigital
(contain all the digits 1 to 9, but not necessarily in order).
And F2749, which contains 575 digits, is the first Fibonacci number for
which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits
AND the last nine digits are 1-9 pandigital, find k.
'''
'''
Idea: brute force, but generate fibonacci numbers using binet's formula (long operations = long!)
'''

import timeit
import decimal

#input a 9 digit number
def isPandigital(n):
    digits = [False] * 9
    while n > 0:
        digits[n % 10 - 1] = True
        n /= 10

    for i in xrange(0, 9):
        if not digits[i]:
            return False

    return True

def keepGoing(n):
    if n < 10 ** 17: #first number with 18 digits
        return True

    temp = n % 10 ** 9
    while n > 10 ** 9:
        n /= 10
    
    return not (isPandigital(temp) and isPandigital(n))

#generates the nth fib number for n >= 2, n0 = 0, n1 = 1
def generateFib(n):
    sqrt5 = decimal.Decimal(5).sqrt();
    unrounded = ((1 + (sqrt5)) ** n - (1 - (sqrt5)) ** n) /((2 ** n) * (sqrt5))
    return int(unrounded)

k = 2
start = timeit.default_timer()

while keepGoing(generateFib(k)):
    k += 1

end = timeit.default_timer()

print "Answer: " , k
print "Time: " , (end - start)

