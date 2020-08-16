"""
Lexicographic Permutations - What is the millionth lexicographic permutation of
the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import math

def perm(arr):
    l = len(arr)
    if l == 1:
        return [[arr[0]]]
    else:
        numPerms = math.factorial(l)
        res = [1] * numPerms
        for i in range(len(arr)):
            start = arr[i]
            tmp = perm(arr[:i]+arr[i+1:])
            for x in range(len(tmp)):
                tmp[x].insert(0, start)
            res[(i*numPerms):((i+1)*numPerms)] = tmp
        return res

# returns the nth lexicographic permutation of the digits in arr
def lexPerm(arr, n):
    arr.sort()

    # we know that arr contains unique digits, so we don't need to filter that
    # out

    # for each digit, there will be numPerm permutations
    numPerm = math.factorial(len(arr) - 1)

    # find which digit we need to start with
    x = numPerm
    index = 0
    while x < n:
        x += numPerm
        index += 1

    # accounts for possibility of there being less than n permutations
    if index > len(arr) - 1:
        return 0
    else:
        first = arr[index]

    # index of permutation which we want
    pos = numPerm - x + n - 1

    # array of the rest of the digits needed to make the permutation
    arr = arr[:index] + arr[(index + 1):]

    # form the permutations
    perms = perm(arr)
    for i in range(len(perms)):
        perms[i].insert(0, first)

    return perms[pos]
