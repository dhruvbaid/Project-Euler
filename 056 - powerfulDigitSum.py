"""
Powerful Digit Sum: for all 1 <= a,b <= 100, what is the maximal digit sum of
a^b?
"""

def maxSum():
    res = 0
    for a in range(1, 101):
        for b in range(1, 101):
            x = a**b
            tmp = 0
            for digit in str(x):
                tmp += int(digit)
            if tmp > res:
                res = tmp
    print(res)
    return
