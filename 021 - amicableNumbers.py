"""
Amicable Numbers - Evaluate the sum of all the amicable numbers under 10000.
"""
import math

def d(n):
    if ((n == 0) or (n == 1)):
        return 0
    else:
        arr = [1]
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if n%i == 0:
                if i == math.floor(math.sqrt(n)):
                    arr.append(i)
                else:
                    arr.append(i)
                    arr.append(n/i)
        return sum(arr)

def sumOfAmicablePairs():
    amicables = []
    for a in range(1, 10001):
        b = d(a)
        if ((d(b) == a) and (a != b)):
            amicables.append(a)
            # amicables.append(b)
    print(amicables)
    return sum(amicables)

print(sumOfAmicablePairs())
