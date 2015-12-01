'''
Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

from timeit import default_timer as timer

start = timer()

#returns whether number can be expressed as the sum of its digits raised to the pth power
def isPowerDigit(n, p):
    goal = n
    nSum = 0
    while n > 0:
        nSum += (n % 10) ** p
        n /= 10
    return nSum == goal

#returns the upper bound for searching this sort of power ie, the greatest power which you
'''
This works since we know for every digit we add after the first, the value of the sum
of the powers can be expressed as n(9 ** p), where n is the number of digits, and p is the
power raised

Meanwhile, the value of the actual number is equal to (n ** 10 - 1)

The rate of change per n of the digit sum is 9 ** p which is a constant
The rate of change per n of the actual number is equal to (n ** 10) * ln(n)

9 ** p = n ^ 10 * ln(n)
'''
def upperBound(p):
    '''
    picture adding 9's the the end of a number. ie 9 -> 99 -> 999
    This is the fastest way to grow the sum of the power of the digits, adding 9 ** p
    every 9 we cocatante

    meanwhile the actual number also grows, 9 -> 99 -> 999

    eventually, when this number is greater than the sum of digits to the pth power, bounds!
    '''
    bound = 9
    digits = 1
    while bound < digits * (9 ** p):
        bound *= 10
        bound += 9
        digits += 1
    return bound

totalSum = 0
#start from 2, since 1 and 0's are not sums and valid for the thing we are searching for
for i in xrange(2, upperBound(5)):
    if isPowerDigit(i, 5):
        totalSum += i

print "Answer : " , totalSum
print "Elapsed: " , (timer() - start) ,"s"


        
    
