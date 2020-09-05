"""
Pandigital Multiples: What is the largest 1 to 9 pandigital 9-digit number that
can be formed as the concatenated product of an integer with (1,2, ... , n)
where n > 1?
"""

def panProduct(num, n):
    res = ''
    for i in range(1, n+1):
        res += str(num * i)
    return int(res)

def isPan(n):
    numLen = len(str(n))
    if numLen != 9:
        return False
    else:
        test = 1
        strNum = str(n)
        for i in range(1, 10):
            if strNum.count(str(i)) != 1:
                test = 0
                break
        if test == 1:
            return True
        else:
            return False

def maxNum(n):
    numDigits = 0
    res = 0
    while numDigits <= 9:
        res += 1
        numDigits = 0
        for i in range(1, n+1):
            numDigits += len(str(res * i))
    return res

def maxPan():
    pans = []
    for n in range(2, 10):
        for num in range(maxNum(n)):
            p = panProduct(num, n)
            if isPan(p):
                pans.append(panProduct(num, n))
    return max(pans)
