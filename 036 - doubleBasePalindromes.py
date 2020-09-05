"""
Double-Base Palindromes: Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.
"""
import math

def isPalindrome(n):
    s = str(n)
    l= len(s)
    if l > 1:
        if l%2 == 0:
            if (int(s[:int(l/2)]) == int(s[int(l/2):][::-1])):
                return True
            else:
                return False
        else:
            if (int(s[:int((l-1)/2)]) == int(s[int((l+1)/2):][::-1])):
                return True
            else:
                return False
    else:
        return True

def baseTwoRep(n):
    maxPow = math.floor(math.log2(n))
    res = []
    for i in range(maxPow + 1):
        res.append(0)
    for power in range(maxPow, -1, -1):
        tmp = 0
        while n - pow(2, power) >= 0:
            n -= pow(2, power)
            tmp += 1
        res[maxPow - power] = tmp
    s = ""
    for x in res:
        s += str(x)
    return int(s)

def doubleBasePalindrome(n):
    res = 0
    for i in range(1, n+1):
        if isPalindrome(i) and isPalindrome(baseTwoRep(i)):
            print(i)
            res += i
    return res
