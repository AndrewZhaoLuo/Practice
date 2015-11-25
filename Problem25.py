# -*- coding: utf-8 -*-
'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

import math

#1000 digits will come from 999 digits come from 998 digits down
Target = 10L ** 999L #999 zeros + 1 one = 1000 digits
index = 2

F1 = 1L
F2 = 1L

while F2 < Target:
    temp = F1 + F2
    F1 = F2
    F2 = temp
    index += 1

print index

