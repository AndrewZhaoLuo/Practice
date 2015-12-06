# -*- coding: cp1252 -*-
'''
A composite is a number containing at least two prime factors.
For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

There are ten composites below thirty containing precisely two,
not necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 10^8, have precisely two, not necessarily distinct,
prime factors?
'''
'''
idea, find all prime numbers below (10^8)/2. Then brute force by checking each combination
for being less than our upper bound. output the number.
'''

from timeit import default_timer as timer

start = timer()

MAX_NUMBER = 10 ** 8

#sieve method, where index represents number, and value whether the number is prime
isPrime = [True] * (((MAX_NUMBER) / 2) + 1)
primes = []
upperBound = int(len(isPrime) ** 0.5)
for i in xrange(2, upperBound):
    if isPrime[i]:
        primes.append(i)
        for r in xrange(i + i, len(isPrime), i): #make sure to go to len(isPrime) and not above
            isPrime[r] = False

for i in xrange(upperBound, len(isPrime)):
    if isPrime[i]:
        primes.append(i)

semiPrimes = 0
#figure out how many total combos
for a in xrange(0, len(primes)):
    for b in xrange(a, len(primes)):
        #stop when go over, if we continue, numbers will get bigger
        if primes[a] * primes[b] > MAX_NUMBER:
            break
        #otherwise, we are multipying two primes, increment semiprimes
        semiPrimes += 1

end = timer()

print "Answer is " + str(semiPrimes)
print "Elapsed : " + str(end - start) + "s"

