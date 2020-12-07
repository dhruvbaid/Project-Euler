"""
Permuted Multiples - find the smallest positive integer, x, such that 2x, 3x,
4x, 5x, and 6x, contain the same digits.
"""

def nToA(n: int):
    return sorted(list(str(n)))

def main():
    n = 1
    while(True):
        if(nToA(n) == nToA(2*n) == nToA(3*n) == nToA(4*n) == nToA(5*n) == nToA(6*n)):
            return n
        else:
            n += 1
