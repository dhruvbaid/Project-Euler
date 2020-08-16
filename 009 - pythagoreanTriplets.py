"""
Special pythagorean triplet: There exists exactly one Pythagorean triplet for
which a + b + c = 1000. Find the product abc.
"""

# pythag : finds pythagorean triplets which sum to n and returns their product
def pythag(n):
    for b in range(1, n+1):
        for c in range(1, n+1):
            if(n*n + 2*b*b + 2*b*c == 2*n*(b+c)):
                return b*c*(n - b - c);
