"""
Distinct Prime Factors - find the first four consecutive integers to have four
distinct prime factors each. Return the first of these numbers.
"""

import math

# have a set of primes globally (saves a TON of space and time)
global primes
primes = {2}

# isPrime : checks if an integer is Prime
def isPrime(n: int):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    else:
        for factor in range(2, int(math.sqrt(n)) + 2):
            if n%factor == 0:
                return False
        return True

# pFac : returns a dict representing the prime factorization of the input int
def pFac(n: int):
    global primes
    
    res = {}
    if isPrime(n):
        res[n] = 1
        return res
    else:
        for i in range(max(primes), n):
            if isPrime(i):
                primes.add(i)
        while n != 1:
            for prime in primes:
                if n%prime == 0:
                    n = n/prime
                    if prime in res.keys():
                        res[prime] += 1
                    else:
                        res[prime] = 1
                    break
        return res

# numDistinct : uses the dict from pFac to return the number of distinct primes
#               in its prime factorization
def numDistinct(n: int):
    return len(pFac(n).keys())

# fourDistinct : maintains a running list of length 4-5 of integers which have
#                4 distinct prime factors, and returns the smallest of 4
#                consecutive integers in this list
def fourDistinct():
    goods = []
    i = 2*3*5*7
    while(True):
        if numDistinct(i) == 4:
            goods.append(i)
            if(((i - 1) in goods) and
               ((i - 2) in goods) and
               ((i - 3) in goods)):
                return (i - 3)
        i += 1
        goods = goods[-4:]

# otherSolution : solution found from the discussion board, runs MUCH faster
def otherSolution():
    Limit = 1000000     # Search under 1 million for now
    factors = [0]*Limit # number of prime factors.
    count=0
    for i in range(2, Limit):
        if factors[i] == 0:
            # i is prime
            count = 0
            val = i
            while val < Limit:
                factors[val] += 1
                val += i
        elif factors[i] == 4:
            count +=1
            if count == 4:
                print(i-3) # First number
                break
        else:
            count = 0
