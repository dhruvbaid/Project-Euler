"""
Square Root Convergents: In the first 1000 expansions of sqrt(2), how many
fractions contain a numerator with more digits than the denominator?
"""

def expansion():
    count = 0
    cur = [3,2]
    for i in range(999):
        cur = [cur[0] + (2*cur[1]), cur[0] + cur[1]]
        # NOTE: these fractions are in their lowest terms, because
        #           gcd(a,b) = 1
        # ==>     gcd(a+b,b) = 1
        # ==>     gcd(b,a+b) = 1
        # ==> gcd(b+a+b,a+b) = 1
        if len(str(cur[0])) > len(str(cur[1])):
            count += 1
    return count
