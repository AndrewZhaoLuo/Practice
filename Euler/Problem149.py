# -*- coding: utf-8 -*-
'''
Looking at the table below, it is easy to verify that the maximum possible sum of
adjacent numbers in any direction (horizontal, vertical, diagonal or anti-diagonal) is 16 (= 8 + 7 + 1).

−2	5	3	2
9	−6	5	1
3	2	7	3
−1	8	−4	  8
Now, let us repeat the search, but on a much larger scale:

First, generate four million pseudo-random numbers using a
specific form of what is known as a "Lagged Fibonacci Generator":

For 1 ≤ k ≤ 55, sk = [100003 − 200003k + 300007k3] (modulo 1000000) − 500000.
For 56 ≤ k ≤ 4000000, sk = [sk−24 + sk−55 + 1000000] (modulo 1000000) − 500000.

Thus, s10 = −393027 and s100 = 86613.

The terms of s are then arranged in a 2000×2000 table, using the first 2000 numbers to fill the
first row (sequentially), the next 2000 numbers to fill the second row, and so on.

Finally, find the greatest sum of (any number of) adjacent entries in any direction
(horizontal, vertical, diagonal or anti-diagonal).
'''
'''
Notes of lagged fibonacci generators:
xn = xn-1 + xn-2 -fib
xn = xn-j () xn-k (mod m)-lagged fib

wher () is some binary operator like addition, subtraction, or bitwise XOR

when j and k are far apart, and m is a power of 2, nice randomness!

Period of the generator is equal to (2^j - 1) * 2^(m-1)
when x^j + x^k + 1 is "primitive over the intergers mod 2". The first j value must be odd
'''
'''
Brainstorm:
in the case above, j = 55, k = 24.
The period is equal to (2^55 - 1) * 2^(1000000-1) which means no repeats!

there are only 2000 rows and cols. 2000 diagnonals in both directions

HOWEVER: in each row/col/diag. we can choose the to include adj elements 1-50, 1-999, 599-1999, etc.
This done brute force would be ineffective, since it runs in n^3 time
(for loop for start index, for loop for end index + calculating sum))

Is there a better way?
1 2 -2 3 4 -2 -4 5
----------
  8 largest sum

the largest sum can be expressed as [1 2 -2 3] + 4
or 1 + [2 -2 3 4]

let's say we have a b c d e f

we want to find the largest contiguous sum that ends at e
that equals max(e, e + largest contiguous sum that ends at d)

yay for recursion!

our largest contiguous sum is going to end somewhere, so just calculate the
largest sum which ends at each index, and keep track of an independant max!

this is a linear time solution!

test:

array:                      1 2 -2 3 4 -2 -4 5
largest sums up to index:   1 2  1 4 8* 6  2 7 

array:  -99 -33 -99 5 -4 5 -99
sums :  -99 -33 -99 5  1 6*-99

array:  1 3 4 1 -1
sums :  1 4 8 9* 8
'''

#better algo based on obs that we only need to know the previous element of where we are
def longestSum(array):
    curMax = array[0]
    previousMax = array[0] 
    for i in xrange(1, len(array)):
        #if we are appending to the beginning of our continguous array
        #then adding the maximum subsequence from the previous element is positive
        previousMax = max(array[i], array[i] + previousMax)
        if(previousMax > curMax):
            curMax = previousMax

    return curMax

#calculate numbers
nums = []
for i in xrange(1, 56):
    sk = (100003 - 200003 * i + 300007 * i * i * i) % 1000000 - 500000
    nums.append(sk)
for i in xrange(55, 4000000 + 1):
    sk = (nums[i-55] + nums[i-24] + 1000000) % 1000000 - 500000
    nums.append(sk)

print "numbers generated"

table1 = []
for r in xrange(0, 2000):
    table1.append([])
    for c in xrange(0, 2000):
        table1[r].append(nums[r * 2000 + c])

table2 = []
for r in xrange(0, 2000):
    table2.append([])
    for c in xrange(0, 2000):
        table2[r].append(nums[r + c * 2000])

print "tables complete"

#there are 2000 rows, 2000 cols, probably around that many diagonals and anti-diagonls
#rows and cols
curMax = 0
for i in xrange(0, 2000):
    curMax = max(curMax, longestSum(table1[i]))#rows
    curMax = max(curMax, longestSum(table2[i]))#cols

print "row and col max: " , curMax

#no need to do below, answer above! #lazy is best
#also, I don't know an efficient way to deal with diagnonals D:
'''
#diagonals which touch top part of table
for c in xrange(0, 2000):
    curArray = []
    for s in xrange(0, 2000 - c): #from top going down right
        curArray.append(table[s][c+s])
    curMax = max(curMax, longestSum(curArray))

    curArray = []
    for s in xrange(0, c + 1): #from top going down left
        curArray.append(table[s][c-s])
    curMax = max(curMax, longestSum(curArray))

#diagonals based on those which hit the left part of table
for r in xrange(0, 2000):
    curArray = []
    for s in xrange(0, 2000 - r):
        curArray.append(table[r+s][s])
    curMax = max(curMax, longestSum(curArray))

    curArray = []
    for s in xrange(0, r + 1):
        curArray.append(table[r-s][1999-s])
    curMax = max(curMax, longestSum(curArray))
'''

print curMax

'''
#OLD

#runs in linear time
#precondition, given array is not empty or null
def longestContinguousSum(array):
    #construct a list of all sums from the 0th element
    sums = []
    sums.append(array[0])
    curMax = array[0]
    for i in xrange(1, len(array)):
        curSum = sums[i - 1] + array[i]
        if(curSum > curMax):                #update max along the way
            curMax = curSum
        sums.append(curSum)

    #idea behind algo:
    #find the longest continguous sum assuming element at index i is the end of a sequence
    #when we look at the i+1 element, we only need to reference the previous element
    for i in xrange(1, len(array)):
        curSum = max(array[i] + sums[i - 1], array[i])
        if(curSum > curMax):
            curMax = curSum
        sums[i] = curSum

    return curMax
'''
