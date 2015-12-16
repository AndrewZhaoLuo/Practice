# -*- coding: cp1252 -*-
'''
It was proposed by Christian Goldbach that every odd composite number can be written
as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
'''
'''
Idea: use sieve to generate primes, then iterate through squares up to a square composite's number
'''

import timeit
start = timeit.default_timer()

UPPER_BOUND = 100000000
isPrime = [False] * 2 + [True] * (UPPER_BOUND)
bound = int(len(isPrime) ** 0.5)
for i in xrange(2, bound + 1):
    if isPrime[i]:
        for a in xrange(i * i, bound + 1, i):
            isPrime[a] = False

#33, is given man  
i = 33
go = True
while go:
    if not isPrime[i]:
        bound = int((i/2) ** 0.5)
        go = False
        for a in xrange(0, bound + 1):
            if isPrime[i - a * a * 2]:
                go = True
    i += 2

print "Answer : " + str(i - 2)
print "Elapsed: " + str(timeit.default_timer() - start)
