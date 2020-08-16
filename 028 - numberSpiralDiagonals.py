"""
Number Spiral Diagonals: What is the sum of the numbers on the diagonals in a
1001 by 1001 spiral formed in the same way?
"""

def spiralSum(n):
    res = 0
    arr = []
    for i in range(1, n+1, 2):
        arr.append(i)
    # arr contains all the odds between 1 and inclusive
    for i in range(len(arr)):
        last = arr[i] * arr[i]
        diff = arr[i] - 1
        if last == 1:
            res += last
        else:
            res += (last + (last - diff) + (last - 2*diff) + (last - 3*diff))
    return res
