"""
Smallest Multiple: What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""

# pFac : returns tuple of prime factors of input integer n
def pFac(n):
    res = ()
    if(n < 2):
        return res;
    else:
        while((n % 2) == 0):
            res += (2, );
            n = n / 2;
        i = 3;
        while(n > 1):
            while((n % i) == 0):
                res += (i, );
                n = n / i;
            i += 2;
        return res;

# factors : returns array containing tuples representing factors of all numbers
#           from 2 to n inclusive
def factors(n):
    arr = []
    for i in range(2, n+1):
        arr.append(pFac(i));
    return arr;

# maxFactor : returns the largest prime factor dividing any integer between 1
#             and n inclusive
def maxFactor(n):
    arr = []
    for i in range(1, n+1):
        arr.append(pFac(i)[-1])
    arr.sort()
    return arr[-1]

# minDiv : combines the previous functions to give the smallest integer which
#          evenly divides all integers from 1 to n inclusive
def minDiv(n):
    totFactors = ()
    for i in factors(n):
        print(i)
        for p in i:
            print(f"Looking at prime {p}");
            currCount = i.count(p)
            totCount = totFactors.count(p)
            if(totCount < currCount):
                d = currCount - totCount;
                for k in range(d):
                    totFactors += (p, );
                print(f"Total Factors: {totFactors}")
    res = 1;
    for i in totFactors:
        res *= i;
    return res;
