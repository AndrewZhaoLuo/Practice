'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13
we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
'''
Brainstorm:
to check if prime, only need to check the number against our list primes
since everything can be factored down to prime numbers!
'''

import timeit

start = timeit.default_timer()

#instantiate 2 as our first prime, makes things ez-r
primes = [2]
cur = 3 #curent number we're looking at

def isPrime(n):
    for i in xrange(0, len(primes)):
        if n % primes[i] == 0:
            return False
    return True

while len(primes) < 10001:
    if(isPrime(cur)):
        primes.append(cur)
    cur += 1

end = timeit.default_timer()
print "Answer : " , primes[len(primes) - 1]
print "Elapsed: " , (end - start), "(s)"

    
