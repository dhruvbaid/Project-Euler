"""
Pandigital Prime: What is the largest n-digit pandigital prime that exists?
"""
import math

# perms : returns all permutations of an input array
def perms(arr):
    if len(arr) == 1:
        return [arr]
    else:
        res = []
        for i in range(len(arr)):
            f = [arr[i]]
            r = arr[:i] + arr[i+1:]
            permRest = perms(r)
            for x in permRest:
                res.append(f + x)
        return res

# pandigitals : returns all pandigital n-digit numbers
def pandigitals(n):
    res = []
    # convert digits [1,n] into an array
    arr = [i for i in range(1, n+1)]
    # get all permutations of the array
    p = perms(arr)
    # convert each permutation into a number and append to result
    for perm in p:
        s = ''
        for i in range(len(perm)):
            s += str(perm[i])
        res.append(int(s))
    return res

# isPrime : tests if an input number is prime
def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif ((str(n)[-1] == '0') or
          (str(n)[-1] == '2') or
          (str(n)[-1] == '4') or
          (str(n)[-1] == '5') or
          (str(n)[-1] == '6') or
          (str(n)[-1] == '8')):
        return False
    else:
        for factor in range(2,math.ceil(math.sqrt(n)) + 1):
            if n % factor == 0:
                return False
        return True

# largestPanPrime : returns largest pandigital Prime number
def largestPanPrime():
    panPrimes = []
    for n in range(1, 10):
        p = pandigitals(n)
        for x in p:
            if isPrime(x):
                panPrimes.append(x)
    return max(panPrimes)
