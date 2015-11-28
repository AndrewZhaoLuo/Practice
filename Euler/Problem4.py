# -*- coding: cp1252 -*-
'''
A palindromic number reads the same both ways. The
largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import timeit

def isPalindrome(str):
    for i in xrange(0, len(str)/2):
        if str[i] != str[len(str) - 1 - i]:
            return False
    return True

start = timeit.default_timer()

largest = 0
for a in xrange(100, 1000):
    for b in xrange(a, 1000):
        result = a * b
        if isPalindrome(str(result)) and result > largest:
            largest = result

end = timeit.default_timer()

print largest
print (start - end)
