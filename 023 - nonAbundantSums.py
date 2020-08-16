"""
Non-Abundant Sums - What is the sum of all integers which cannot be expressed as
the sum of two abundant numbers?
"""
import math

# d : returns sum of proper divisors of a number
def d(n):
    res = 0
    z = 1
    while z < (math.floor(math.sqrt(n)) + 1):
        if(n%z == 0):
            if(z == math.sqrt(n)):
                res += z
            else:
                res += (z + n/z)
        z += 1
    res -= n
    res = int(res)
    return res

# abundant : returns list of abundant numbers <= n
def abundant(n):
    a = [2] * (n+1)
    for i in range(n+1):
        if a[i] == 2:
            if d(i) > i:
                a[i] = 1
                for k in range(2, math.floor(n/i)):
                    a[k * i] = 1
    res = []
    for i in range(n):
        if a[i] == 1:
            res.append(i)
    return res

# main : returns sum integers <= n which cannot be written as the sum of two
#        abundant numbers
def main(n):
    # nums is the set of all numbers from 1 to n inclusive
    nums = {0}
    for i in range(n):
        nums.add(i+1)
    nums.remove(0)
        
    # list of abundants
    abundants = abundant(n)
    l = len(abundants)
    print("Abundants done")

    # sums is the set of all sums of 2 abundants
    sums = {0}
    for i in range(len(abundants)):
        for j in range(i, len(abundants)):
            s = abundants[i] + abundants[j]
            if s <= n:
                sums.add(s)
    sums.remove(0)
    
    return(sum(nums - sums))
