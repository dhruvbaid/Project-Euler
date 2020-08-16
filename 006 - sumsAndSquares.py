"""
Sum Square Difference: Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of their sum.
"""

# diff : returns the difference between the sum of the squares of the first n
#        hundred natural numbers and the square of their sum
def diff(n):
    return (int)(abs((n*(n+1)*(2*n + 1)/6) - ((n*(n+1)/2) * (n*(n+1)/2))));

"""
Solution takes advantage of the formulae for sums of naturals and sums of
squares of naturals
"""
