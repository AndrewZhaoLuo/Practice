# -*- coding: utf-8 -*-
from timeit import default_timer as timer

start = timer()

#index = number when starting and run collatz
#element at index = number of iterations before hitting 1
numbers = [-1] * 1000001

numbers[0] = 0
numbers[1] = 1

#given a number n returns the number of iterations of collatz to reach
def collatz(n):
    #base cases
    if n < len(numbers) and numbers[n] != -1:
        return numbers[n]

    #recursive cases for hailstone under 1000000
    result = 0
    if(n % 2 == 0):
        result = 1 + collatz(n / 2)
    else:
        result = 1 + collatz(3 * n + 1)

    if(n < len(numbers)):
        numbers[n] = result
        return numbers[n]
    else:
        return result
    
#basic idea, run collatz on all numbers under 1000000 and memoize known sequence lengths along the way
chainSize = 1
largestNum = 1
for i in xrange(1, 1000000):
    result = collatz(i)
    if(result > chainSize):
        chainSize = result
        largestNum = i

end = timer()

print "largest num with longest chain: " + str(largestNum)
print str(end - start) + " ms"
