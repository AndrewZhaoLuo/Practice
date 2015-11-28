# -*- coding: utf-8 -*-
'''
A natural number, N, that can be written as the sum and product of a given set of at least
two natural numbers,{a1, a2, ... , ak} is called a product-sum
number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a
minimal product-sum number. The minimal product-sum numbers for sets of size,
k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30;
note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is
{4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?
'''
'''
Brainstorm

for k = n

x1 * x2 * x3 * x4 ... *xn = x1 + x2 + x3 + x4 .... + xn = p
where x1 >= x2 >= x3 >= x4 .... >= xn

Furthermore:
x2 * x3 * x4 ... *xn = 1 + (x2 + x3 + x4 .... + xn)/x1 = p / x1
(x2 + x3 + x4 .... + xn)/x1 must be an integer since
x2 * x3 * x4 ... *xn - 1 is an integer

x2 * x3 * x4 ... *xn = p/x1 this is a subproblem!

Therefore, x2 + x3 + x4 .... + xn is a multiple of x1

Furthermore, to minimize the product sum p, x1 should be as low as possible, since the
minimum value for x2+x3+x4...+xn is minimized that way
'''

totSum = 0 
#for k in xrange(1, 12000 + 1)
