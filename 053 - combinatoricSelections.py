"""
Combinatoric Selections - how many, not necessarily distinct, values of nCr for
1 <= n <= 100 are greater than 1,000,000?
"""
from math import factorial as f

# nCr : returns binomial coefficient (n,r) == nCr
def nCr(n: int, r: int):
    if(r < 0):
        exit(0)
    elif(r > n):
        exit(0)
    else:
        return int(f(n)/(f(r)*f(n - r)))

# main : loops through binomial coefficients and returns number of them greater
#        than 1,000,000. Uses symmetry of coefficients ((n,r) = (n,n-r)) to
#        break loops as early as possible.
def main():
    res = 0
    for n in range(1, 101):
        if n%2 == 0:
            for r in range(0, int(n / 2) + 1):
                if nCr(n, r) > 1000000:
                    if r == int(n / 2):
                        res += 1
                        break
                    else:
                        res += (2*(int(n / 2) - r)) + 1
                        break
        else:
            for r in range(0, int(n / 2) + 1):
                if nCr(n, r) > 1000000:
                    res += 2*(int(n / 2) - r + 1)
                    break
    return res
