# -*- coding: cp1252 -*-
'''
Find the unique positive integer whose square has the form
1_2_3_4_5_6_7_8_9_0,

where each “_” is a single digit.
'''
'''
Note, must have at the minimum 2 0's!
'''
import timeit

start = timeit.default_timer()

#given an integer, return true if the square fits the unique positive integer format
def itWorks(n):
    num = n * n
    for i in xrange(9, 1, -1):
        if num % 10 != i:
            return False
        num /= 100

    return True
    

upperBound = int(19293949596979899 ** 0.5)
lowerBound = int(10203040506070809 ** 0.5)

count = 0
for i in xrange(lowerBound, upperBound + 1):
    if itWorks(i):
        count += 1
        
print "Answer : " + str(count)
print "Elapsed: " + str(timeit.default_timer() - start) + "s"
                                    
                                    
        
