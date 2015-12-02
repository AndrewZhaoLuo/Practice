# -*- coding: utf-8 -*-
'''
A number chain is created by continuously adding the square of the digits in a number
to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''
'''
idea, if we know 85 will arrive at 89, we know if we hit 85 we will eventually go to 89
likewise, if we hit 145, that leads to 89

Therefore, keep track of which numbers hit 1 and 0
'''
from timeit import default_timer as timer
start = timer()

UPPER_BOUND = 10000000
HIT_1 = 1
HIT_89 = 2

#index 1-9999999, represent all numbers below 10 million
numbers = [0] * UPPER_BOUND
numbers[89] = HIT_89
numbers[1] = HIT_1

def squareDigits(n):
    tot = 0
    while n > 0:
        tot += (n % 10) ** 2
        n /= 10
    return tot

def cycle(n):
    #base case, find a number that hits one of our targets
    if numbers[n] == HIT_1:
        return HIT_1
    elif numbers[n] == HIT_89:
        return HIT_89

    #otherwise cycle
    numbers[n] = cycle(squareDigits(n))
    return numbers[n]

tot = 0
for i in xrange(1, UPPER_BOUND):
    if cycle(i) == HIT_89:
        tot += 1

end = timer()
print "Answer : " , tot
print "Elapsed:" , (end - start) , "s"
