'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to
n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
'''
use the sieve. the largest pandigital number we need to check is
987,654,321.

EXCEPT IT ISN'T!
As a pandigital number that uses all the digits will be divisible by 3

(9 + 1) * 9/2 = 45!
Therefore, the largest possible number we must check is 98765432
'''
'''
Use sieve method, then iterate from the top of our sieve, stop at our first pandigital number
'''

from timeit import default_timer as timer
start = timer()

UPPER_BOUND = 98765432
SIEVE_BOUND = int(UPPER_BOUND ** 0.5)

def isPandigital(n):
    order = 0
    while n >= 10 ** order:
        order += 1

    #index (1-based) represents whether digits has been reached yet
    digits = [True] + [False] * (order)
    while n > 0:
        if n % 10 >= len(digits) or digits[n % 10]:  #already hit digit :(
            return False
        digits[n % 10] = True
        n /= 10

    return True

isPrime = [True] * UPPER_BOUND
for i in xrange(2, SIEVE_BOUND):
    if isPrime[i]:
        for a in xrange(i + i, UPPER_BOUND, i):
            isPrime[a] = False

i = len(isPrime) - 1
while not(isPrime[i] and isPandigital(i)):
    i -= 1

print "Answer: " + str(i)
print "Elapsed: " + str(timer() - start)
