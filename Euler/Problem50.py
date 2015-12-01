'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains
21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''
'''
IDEA: keep track of sums bruh
'''

class Prime:
    def __init__(n):
        

UPPER_BOUND = 1000000

sieve = [True] * (UPPER_BOUND + 1) #1 based index (skip one, one is evil, two is first prime)

for i in xrange(2, UPPER_BOUND + 1):
    if sieve[i]:
        for c in xrange(i + i, UPPER_BOUND + 1, i):
            sieve[c] = False

primes = []
for i in xrange(2, UPPER_BOUND + 1):
    if sieve[i]:
        primes.append(i)

equivalentPrimes = [] #the number of equivalent primes you add by adding this prime
                      #E.g. 41 would be 6 since 41 = 2 + 3 + 5 + 7 + 11 +13
                      #6 numbers!

for i in xrange(0, len(prime)):
    count = 0
    tot = primes[i]
    for c in xrange(0, i):
        
