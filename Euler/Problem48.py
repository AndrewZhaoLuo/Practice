'''
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

'''
idea, multiply continually, but only keep the last ten digits!
'''

from timeit import default_timer as timer

start = timer()

seriesSum = 0 #only last 10 digits
for i in xrange(1, 1000+1):
    prod = 1
    for c in xrange(0, i):
        prod *= i
        prod = prod % 10 ** 10 #guarantees only a ten digit product remains
    seriesSum += prod
    seriesSum = seriesSum % 10 ** 10

print "Answer: ", seriesSum
print "Elapsed:", (timer() - start)
