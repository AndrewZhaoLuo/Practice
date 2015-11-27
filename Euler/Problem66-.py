# -*- coding: utf-8 -*-
'''
Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

32 – 2×22 = 1
22 – 3×12 = 1
92 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the
largest value of x is obtained.
'''

'''
Brainstorm:
pretty simple

rearrangining variables we find that (x^2 - 1)/D = y^2

therefore, iterate through D, then iterate through x until a value fufills the equation above
(that is x^2 - 1 is square).

skip values of D which are square (hint given) keeping track of the maximum x hit/

A diophantine equation cannot have coefficient values of 0, so (x^2 - 1)/D != 0

def isSquare(n):
    return (n ** 0.5) == int(n ** 0.5)

maxX = 0
for D in xrange(1, 1000 + 1):
    print D
    if not isSquare(D):
        x = 1
        while not isSquare(float(x * x - 1)/D) or float(x * x - 1)/D == 0:
            if(D == 61):
                print x
            x += 1
        maxX = max(maxX, x)

got hung up at D = 61

alternate solution
'''



print maxX
