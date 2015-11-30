'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
#bruteforce
from timeit import default_timer
start = default_timer()

for c in xrange(1, 1001):
    for b in xrange((1000-c)/2 + 1, c): #bounds guarantee a < b < c
        a = 1000 - b - c
        if c ** 2 == a ** 2 + b ** 2:
            print "Answer  : " , (a*b*c)
            print "Elapsed : " , (default_timer() - start) , "s"
