"""
Pandigital Products: We shall say that an n-digit number is pandigital if it
makes use of all the digits 1 to n exactly once; for example, the 5-digit
number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""

# rearrange : return an array containing all possible rearrangements of the
#             input array, assuming the input array contains unique elements
def rearrange(arr):
    res = []
    if len(arr) == 1:
        res.append(arr)
        return res
    else:
        for i in range(len(arr)):
            first = [arr[i]]
            rest = arr[:i] + arr[i+1:]
            # print(f"First: {first}, Rest: {rest}")
            rearranged_rest = rearrange(rest)
            # print(rearranged_rest)
            for x in rearranged_rest:
                res.append(first + x)
        return res

def main():
    res = 0
    products = []
    # simple calculations show that the product has to be exactly 4 digits
    for product in range(1234,9876 + 1):
        # append valid products (distinct, nonzero digits) to the products array
        s = str(product)
        a = list(s)
        count = 1
        for digit in s:
            if a.count(digit) > 1:
                # ignore 4-digit numbers with repeated digits
                count = 0
        if a.count('0') > 0:
            # ignore 4-digit numbers containing 0
            count = 0
        if count != 0:
            products.append(product)
    # print(products)
    for p in products:
        remaining = []
        s = str(p)
        for digit in range(1,10):
            if str(digit) not in s:
                remaining.append(digit)
        # remaining now contains the other 5 digits which need to be rearranged
        # and multiplied to form the product
        r = rearrange(remaining)
        for order in r:
            d1,d2,d3,d4,d5 = order[0],order[1],order[2],order[3],order[4]
            if (((d1 * (1000*d2 + 100*d3 + 10*d4 + d5)) == p) or
                (((10*d1 + d2) * (100*d3 + 10*d4 + d5)) == p) or
                (((100*d1 + 10*d2 + d3) * (10*d4 + d5)) == p) or
                (((1000*d1 + 100*d2 + 10*d3 + d4) * d5) == p)):
                   res += p
                   break
            """
            Uncommnt to see the actual multiplicand/multiplier/product identity
            
            if (d1 * (1000*d2 + 100*d3 + 10*d4 + d5)) == p:
                print(f"{d1}*{d2}{d3}{d4}{d5} = {p}")
                res += p
                break
            elif ((10*d1 + d2) * (100*d3 + 10*d4 + d5)) == p:
                print(f"{d1}{d2}*{d3}{d4}{d5} = {p}")
                res += p
                break
            elif ((100*d1 + 10*d2 + d3) * (10*d4 + d5)) == p:
                print(f"{d1}{d2}{d3}*{d4}{d5} = {p}")
                res += p
                break
            elif ((1000*d1 + 100*d2 + 10*d3 + d4) * d5) == p:
                print(f"{d1}{d2}{d3}{d4}*{d5} = {p}")
                res += p
                break
            else:
                continue
            """
    return res
