"""
Goldbach's Other Conjecture - Find the smallest odd composite which cannot be
written as the sum of a prime and twice a square
"""

import math

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

def goldbachConjecture():
    i = 9
    expressible = True
    primes = [2, 3, 5, 7]
    while(expressible):
        i += 2
        if isPrime(i):
            primes.append(i)
        else:
            # i is composite - check if it can be expressed as p + 2n^2
            # print(primes)
            for prime in primes:
                n1 = math.sqrt(int((i - prime)/2))
                n2 = int(n1)
                if n1 == n2:
                    # print(f"n1 = {n1} = {n2} = n2")
                    expressible = True
                    break
                else:
                    if prime == primes[-1]:
                        return i
