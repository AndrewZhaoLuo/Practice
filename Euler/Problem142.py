# -*- coding: utf-8 -*-
'''
Find the smallest x + y + z with integers x > y > z > 0 such that
x + y, x − y, x + z, x − z, y + z, y − z are all perfect squares.
'''
'''
Brainstorming

the nth perfect square can be represented as the sum of the first n odd numbers

call:
a = x + y
b = x - y
c = x + z
d = x - z
e = y + z
f = y - z

where a - f are all perfect squares

a + b = 2x
c + d = 2x
e + f = 2y

(a + c) * 2 = 4x + 2y + 2z
(a + c) * 2 - (a + b) = 2x + 2y + 2z
(a + c) - (a + b) / 2 = x + y + z

a > c > b

choose some 'a' which is a perfect square. choose some 'c' up to 'a' and some 'b' up to 'c'
we can obtain x using the equation
x = (a + b)/2
y = (a - b)/2
z = c - x

then check if d-f are perfect squares
'''
#step 1: the maximum number of squares that can be referenced is 6

def isInteger(n):
    return n - int(n) == 0

def isSquare(n):
    return isInteger(n ** 0.5)

#Precondition: a, b, c must be perfect squares where a > c > b
def keepGoing(a, b, c):
    #a and b must be same parity for x and y to be integers!
    if (a + b) % 2 == 1:
        return True

    x = (a + b) / 2
    y = (a - b) / 2
    z = c - x

    if not (x > y and y > z and z > 0):
        return True

    d = x - z
    e = y + z
    f = y - z

    #print "x: ", x, " y: ", y, " z: ", z

    #a, b, and c are already squares, check d-f
    return not (isSquare(d) and isSquare(e) and isSquare(f))

#memoize previously found squares
#a > c > b
squares = [1];
count = 3
cont = True

while cont:
    count += 1

    #memoize!
    if(isSquare(count)):
        squares.append(count)
        a = len(squares) - 1
        for c in xrange(1, a):
            for b in xrange(0, c):
                cont = keepGoing(squares[a], squares[b], squares[c])
                if not cont: #record
                    print "a: " , squares[a]
                    print "b: " , squares[b]
                    print "c: " , squares[c]
                    print "x: ", (squares[a] + squares[b])/2 
                    print "y: ", (squares[a] - squares[b])/2 
                    print "z: ", (squares[c] - (squares[a] + squares[b])/2)









    
