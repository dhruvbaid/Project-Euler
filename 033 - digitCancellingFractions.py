"""
Digit-Cancelling Fractions: The fraction 49/98 is a curious fraction, as an
inexperienced mathematician in attempting to simplify it may incorrectly believe
that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator.
"""

def main():
    res = 1
    num = 1
    den = 1
    for n in range(10,100):
        for d in range(n+1, 100):
            if (n%10 != 0) or (d%10 != 0):
                # no longer a trivial fraction
                numList = list(str(n))
                denList = list(str(d))
                for digit in numList:
                    if digit in denList:
                        numList.remove(digit)
                        denList.remove(digit)
                if ((len(numList) < 2) and
                    (len(denList) < 2) and
                    (int(denList[0]) != 0) and
                    (n/d == int(numList[0])/int(denList[0]))):
                    res *= int(numList[0])/int(denList[0])
                    num *= int(numList[0])
                    den *= int(denList[0])
    for f in range(2, num):
        while (num%f == 0) and (den%f == 0):
            num = num/f
            den = den/f
    return int(den)
