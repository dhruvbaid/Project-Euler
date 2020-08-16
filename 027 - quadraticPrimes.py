"""
Quadratic Primes: Find the product of the coefficients, a and b, for the
quadratic expression that produces the maximum number of primes for consecutive
values of n, starting with n=0.
"""
import math

def isPrime(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

def q(a, b, n):
    return ((n * n) + (a * n) + b)

def quadPrimes():
    arr = []
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            n = 0
            tmp = q(a, b, n)
            while((tmp > 0) and isPrime(tmp)):
                n += 1
                tmp = q(a, b, n)
            arr.append(n)
    index = arr.index(max(arr))
    a_index = index // 2001
    b_index = index % 2001
    a_val = a_index - 1000
    b_val = b_index - 1000
    return (a_val * b_val)
