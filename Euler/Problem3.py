import math

'''
Q:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600,851,475,143?
'''

'''
Rationale:
Keep dividing our large number until what we have left is a prime number
doing so removes the smallest factors first, allowing the cream to rise to the top
'''

num = 600851475143L     #a long int is required to store the size of our number
numSqrt = math.sqrt(num)#also only need to check up to the sqrt of our current num
latestPrime = 2         #prime factorizing in order - do not need to recheck lower value primes


while latestPrime < numSqrt:
    if num % latestPrime == 0:
        num /= latestPrime
        numSqrt = math.sqrt(num) #update sqrt bounds!
    else:
        latestPrime += 1         #check next factor (guaranteed prime since previous factors
                                 #have been factored already)

print num
