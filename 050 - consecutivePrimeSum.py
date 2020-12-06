"""
Consecutive Prime Sum - which prime, below one-million, can be written as the
sum of the most consecutive primes?
"""
from math import sqrt

def sieveOfE(n: int):
    primes = []
    nums = [i for i in range(0, n+1)]
    prime = [-1 for i in range(0, n+1)]
    prime[0] = 0
    prime[1] = 0
    for i in range(2, len(prime)):
        if prime[i] == -1:
            # i is prime
            prime[i] = 1
            for k in range(2, int(n/i) + 1):
                prime[i*k] = 0
    for i in range(len(prime)):
        if prime[i] == 1:
            primes.append(nums[i])
    return primes

def maxConSum(nMax: int):
    primes = sieveOfE(nMax)

    # find upper limit on number of terms
    tMax = 1
    s = sum(primes[:tMax])
    while(s <= primes[-1]):
        tMax += 1
        s = sum(primes[:tMax])
    tMax -= 1

    # check sequences of length nTerms in reverse order from tMax to 2
    for nTerms in range(tMax, 2, -1):
        for i in range(int(len(primes)/nTerms)):
            if(nTerms * primes[i] <= primes[-1]):
                terms = primes[i:i + nTerms]
                if sum(terms) in primes:
                    res = (nTerms, sum(terms))
                    return res
