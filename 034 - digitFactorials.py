"""
Digit Factorials: Find the sum of all numbers which are equal to the sum of the
factorials of their digits.
"""

def factorial(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        res = 1
        while n > 0:
            res *= n
            n -= 1
        return res

def main():
    # store factorials 0! through 9! in a dictionary for easier access
    d = {0:1}
    for i in range(1,10):
        d[i] = factorial(i)

    # store success cases in arr
    arr = []
    for i in range(1, 999999):
        tmp = 0
        digits = list(str(i))
        for digit in digits:
            tmp += d[int(digit)]
        if tmp == i:
            arr.append(i)
    return arr
