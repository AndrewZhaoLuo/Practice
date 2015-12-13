# -*- coding: utf-8 -*-
'''
If we calculate a2 mod 6 for 0 ≤ a ≤ 5 we get: 0,1,4,3,4,1.

The largest value of a such that a^2 ≡ a mod 6 is 4.
Let's call M(n) the largest value of a < n such that a2 ≡ a (mod n).
So M(6) = 4.

Find ∑M(n) for 1 ≤ n ≤ 10^7.
'''

'''
Brute force:

iterate (10^7) ** 2, and record the values.
then iterate through

note: use chinese remainder theoerem to determine the minimum numbers to obtain a modulus at
a certain modulus, then iterate
'''

from timeit import default_timer as timer

start = timer()

UPPER_BOUND = 10 ** 7
for a in xrange(1, UPPER_BOUND + 1):
    n = 100
    #for b in xrange(1, UPPER_BOUND + 1):
        #n = 100

end = timer()

print (end - start)
