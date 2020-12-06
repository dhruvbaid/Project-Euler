"""
Self Powers - find the last 10 digits of 1^1 + ... + 1000^1000
"""

def selfPower(n: int):
    if(n < 1):
        print("Check input")
        exit(0)
    series = 0
    for i in range(1, n+1):
        series += (i ** i)%(10**10)
    print(series % (10 ** 10))
