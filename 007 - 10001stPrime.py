"""
10001st Prime: What is the 10,001st prime number?
"""

# pFac : returns tuple of prime factors of input integer n
def pFac(n):
    res = ()
    if(n < 2):
        return res;
    else:
        while((n % 2) == 0):
            res += (2, );
            n = n / 2;
        i = 3;
        while(n > 1):
            while((n % i) == 0):
                res += (i, );
                n = n / i;
            i += 2;
        return res;

def arrPrimes(n):
    i = 0;
    arr = [2];
    while i < (n - 1):
        currPrime = arr[0];
        newPrime = currPrime + 1;
        while (pFac(newPrime).count(newPrime) != 1):
            newPrime += 1;
        arr = [newPrime];
        i += 1;
    return arr[0];
