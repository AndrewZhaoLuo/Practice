'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

'''
Brute force! with a few optimizations from number theory
'''

from timeit import default_timer as timer

start = timer()
primes = [2]

#all numbers can be broken down to prime factorizations
#only need to check primes as factors for our numbers
def isPrime(n):
    for i in xrange(0, len(primes)):
        if n % primes[i] == 0:
            return False
        if primes[i] > n ** 0.5: #only need to check up to sqrt of our number for factors!
            return True
    return True

for i in xrange(3, 2000001):
    if isPrime(i):
        primes.append(i)

tot = 0
for i in xrange(0, len(primes)):
    tot += primes[i]

print "Answer : " , tot
print "Elapsed: " , (timer() - start)
