"""
Truncatable Primes: The number 3797 has an interesting property. Being prime
itself, it is possible to continuously remove digits from left to right, and
remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import math

# isPrime : tests if an input number is prime by checking divisibility against
#           all integers up to and including its square root
def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for factor in range(2,math.ceil(math.sqrt(n)) + 1):
            if n % factor == 0:
                return False
        return True

# makeUnique : returns an array containing only the unique elements of the input
#              array
def makeUnique(arr):
    for x in arr:
        numX = arr.count(x)
        if arr.count(x) > 1:
            for i in range(numX - 1):
                arr.remove(x)
    return arr

# getTruncated : returns an array containing all the left- and right-truncated
#                numbers from a given input number
def getTruncated(n):
    res = []
    numArr = list(str(n))
    arrLen = len(numArr)
    for i in range(arrLen):
        tL = ""
        for x in numArr[i:]:
            tL += x
        res.append(int(tL))
        tR = ""
        for y in numArr[:arrLen - i]:
            tR += y
        res.append(int(tR))
    return makeUnique(res)

# truncatable : returns the sum of all 11 truncatable primes (excluding 2,3,5,7)
def truncatable():
    count = 0
    res = 0
    num = 1
    while count < 11:
        if ((num == 2) or (num == 3) or (num == 5) or (num == 7)):
            # considered non-truncatable by definition; ignored
            num += 1
        else:
            if isPrime(num):
                # check for truncatability
                truncated = getTruncated(num)
                test = 1
                for n in truncated:
                    if (not isPrime(n)):
                        test = 0
                        break
                if test == 1:
                    # this prime yields primes when truncated in both directions
                    count += 1
                    res += num
                    num += 1
                else:
                    # one (or more) of the truncated numbers is not prime
                    num += 1
            else:
                # number is not even prime; ignored.
                num += 1
    return res
