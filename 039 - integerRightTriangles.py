"""
Integer Right Triangles: If p is the perimeter of a right angle triangle with
integral length sides, {a,b,c}, there are exactly three solutions for p = 120:
{20,48,52}, {24,45,51}, {30,40,50}.

For which value of p ≤ 1000, is the number of solutions maximised?
"""
import math

def numSolutions(p):
    count = 0
    for a in range(1, math.ceil(p/3) + 1):
        for b in range(a+1, math.ceil(p/2) + 1):
            c = p - a - b
            if c > 0:
                if ((a*a) + (b*b) == (c*c)):
                    count += 1
    return count

def maxSolutions():
    d = {120: 3}
    for p in range(1, 1001):
        x = numSolutions(p)
        if x > 3:
            d[p] = numSolutions(p)
    print(d)
    return sorted(d, key = lambda x: d[x])[-1]
