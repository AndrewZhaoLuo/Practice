'''
If we list all the natural numbers below 10 that are
multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

import timeit

start = timeit.default_timer()

tot = 0
for i in xrange(1, 1000):
    if(i % 3 == 0 or i % 5 == 0):
        tot += i

end = timeit.default_timer()

print "Answer  : " , tot
print "Time(ms): " , (end-start)
