"""
Prime Permutations - find the arithmetic sequence of 4-digit primes whose digits
are permutations of one another
"""
from math import sqrt

def isPrime(n: int):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    else:
        for factor in range(2, int(sqrt(n)) + 2):
            if n%factor == 0:
                return False
        return True

def pPerms():
    primes_4digit = []
    allPerms = []
    validPerms = []

    # get list of 4-digit primes
    for i in range(1000,10000):
        if isPrime(i):
            primes_4digit.append(i)

    # get list of ALL primes which have the same digits (permutations)
    for i in range(len(primes_4digit)):
        perms = set()
        cur = set(list(str(primes_4digit[i])))
        for j in range(i+1, len(primes_4digit)):
            tmp = set(list(str(primes_4digit[j])))
            if tmp == cur:
                perms.add(primes_4digit[i])
                perms.add(primes_4digit[j])
        if len(perms) >= 3:
            perms = sorted(perms)
            allPerms.append(perms)

    # check for any ascending sequence in each permutation, append to list
    for perm in allPerms:
        for i in range(len(perm)):
            for j in range(i+1, len(perm)):
                for k in range(j+1, len(perm)):
                    if((perm[j] - perm[i]) == (perm[k] - perm[j])):
                        tmp = [perm[i], perm[j], perm[k]]
                        if tmp not in validPerms:
                            validPerms.append(tmp)

    # print out the list of valid permutations
    print(validPerms)
