# -*- coding: utf-8 -*-
'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers
and the square of the sum.
'''

from timeit import default_timer as timer
#only 100 numbers? BRUTE FORCE
start = timer()

intSum = 0
squSum = 0
for i in xrange(1, 100 + 1):
    intSum += i
    squSum += i * i

end = timer()

print "Answer: " , ((intSum ** 2) - squSum)
print "Elapsed:" , (end - start), "(s)"
    
