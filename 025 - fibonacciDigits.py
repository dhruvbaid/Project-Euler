"""
Fibonacci Digits - What is the index of the first term in the Fibonacci sequence
which contains 1000 digits?
"""

def firstIndex(n):
    res = 2
    x = 1
    y = 1
    while y < (10 ** (n - 1)):
        tmp = x + y
        x = y
        y = tmp
        res += 1
    return res
