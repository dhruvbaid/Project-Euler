"""
Triangular, Pentagonal, and Hexagonal: if we define
    T(n) = n(n+1)/2
    P(n) = n(3n - 1)/2
    H(n) = n(2n - 1)
then it is clear that T(285) = P(165) = H(143). Find the next triangle number
that is also Pentagonal and Hexagonal.
"""

# t : returns triangular number
def t(n: int):
    return int((n * (n + 1))/2)

# p : returns pentagonal number
def p(n: int):
    return int((n * ((3 * n) - 1))/2)

# h : returns hexagonal number
def h(n: int):
    return (n * ((2 * n) - 1))

# tph : checks if hexagonal number is in a list of triangulars and hexagonals
def tph():
    n_h = 1
    triangulars = []
    pentagonals = []
    n_t = 1
    n_p = 1
    while(True):
        he = h(n_h)
        while(t(n_t) <= he):
            triangulars.append(t(n_t))
            n_t += 1
        while(p(n_p) <= he):
            pentagonals.append(p(n_p))
            n_p += 1
        if((he in triangulars) and (he in pentagonals)):
            print(he)
            if(he > 40755):
                return he
        n_h += 1
        triangulars = []
        pentagonals = []
