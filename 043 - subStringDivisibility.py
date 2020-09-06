"""
Sub-String Divisibility: The number, 1406357289, is a 0 to 9 pandigital number
because it is made up of each of the digits 0 to 9 in some order, but it also
has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""
import math

# perms : returns all permutations of an input array
def perms(arr):
    if len(arr) == 1:
        return [arr]
    else:
        res = []
        for i in range(len(arr)):
            f = [arr[i]]
            r = arr[:i] + arr[i+1:]
            permRest = perms(r)
            for x in permRest:
                res.append(f + x)
        return res

# pandigitals : returns all 0-n inclusive pandigital (n+1)-digit numbers
def pandigitals(n):
    res = []
    # convert digits [1,n] into an array
    arr = [str(i) for i in range(n+1)]
    # get all permutations of the array
    p = perms(arr)
    # convert each permutation into a number and append to result
    for perm in p:
        s = ''
        for i in range(len(perm)):
            s += perm[i]
        res.append(s)
    return res

# isSpecial : tests if an input number (as a string) has the requisite property
def isSpecial(n: str):
    arrNum = list(n)
    n1 = int(arrNum[1] + arrNum[2] + arrNum[3])
    n2 = int(arrNum[2] + arrNum[3] + arrNum[4])
    n3 = int(arrNum[3] + arrNum[4] + arrNum[5])
    n4 = int(arrNum[4] + arrNum[5] + arrNum[6])
    n5 = int(arrNum[5] + arrNum[6] + arrNum[7])
    n6 = int(arrNum[6] + arrNum[7] + arrNum[8])
    n7 = int(arrNum[7] + arrNum[8] + arrNum[9])
    if ((n1 % 2 == 0) and
        (n2 % 3 == 0) and
        (n3 % 5 == 0) and
        (n4 % 7 == 0) and
        (n5 % 11 == 0) and
        (n6 % 13 == 0) and
        (n7 % 17 == 0)):
        return True
    else:
        return False

# main : returns sum of all 0-9 pandigital numbers with the property
def main():
    res = 0
    p = pandigitals(9)
    print("done")
    for x in p:
        if isSpecial(x):
            print(x)
            res += int(x)
    return res
