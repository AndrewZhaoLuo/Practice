'''
2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
'''
'''
Brainstorm:

primes from 1 - 20
2, 3, 5, 7, 11, 13, 17

get a max count of prime factors out of first 20 numbers (exclude 1 since everything is divisible)
and multiple!
'''

primes = [2, 3, 5, 7, 11, 13, 17, 19, 21]
primeCount = [0] * len(primes)

for i in xrange(2, 21):
    print i
    cur = i
    div = 0
    while cur >= primes[div]:
        count = 0
        while(cur % primes[div] == 0):
            count += 1
            cur /= primes[div]
        primeCount[div] = max(count, primeCount[div])
        div += 1

result = 1
for i in xrange(0, len(primes)):
    result *= primes[i] ** primeCount[i]

print result
