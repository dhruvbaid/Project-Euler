"""
Circular Primes: The number, 197, is called a circular prime because all
rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
"""

def primes(n):
    isPrime = []
    for i in range(n+1):
        isPrime.append(-1)
    isPrime[0] = 0
    isPrime[1] = 0
    for i in range(2,n+1):
        if isPrime[i] == -1:
            isPrime[i] = 1
            k = i*2
            while k < n+1:
                isPrime[k] = 0
                k += i
    primes = []
    for i in range(n+1):
        if isPrime[i] == 1:
            primes.append(i)
    return primes

def makeUnique(arr):
    for x in arr:
        num = arr.count(x)
        if num > 1:
            for r in range(num - 1):
                arr.remove(x)
    return arr

def main(n):
    res = []
    p = primes(n)
    for prime in p:
        strPrime = str(prime)
        if ((prime not in res) and
            (((prime != 2) and ('2' not in strPrime)) or (prime == 2)) and
            ('4' not in strPrime) and
            ('6' not in strPrime) and
            ('8' not in strPrime) and
            (((prime != 5) and ('5' not in strPrime)) or (prime == 5)) and
            ('0' not in strPrime)):
            arrPrime = list(str(prime))
            primeLen = len(arrPrime)
            tmp = []
            for i in range(primeLen):
                circ = arrPrime[i:] + arrPrime[:i]
                s = ''
                for j in range(len(circ)):
                    s += circ[j]
                tmp.append(int(s))
            count = 0
            circulars = []
            for x in tmp:
                if x in p:
                    count += 1
                    circulars.append(x)
            if count == len(tmp):
                # print(makeUnique(circulars))
                res += makeUnique(circulars)
    return res
