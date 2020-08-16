"""
sum of primes: find the sum of all primes less than 2,000,000
"""
import math

#sieveOfE: uses sieve of Eratosthenes to find primes less than or equal to n
def sieveOfE(n):
	arr = []
	for x in range(2, n+1):
		arr.append(x)
	for x in arr:
		for j in arr:
			if((j != x) and (j%x == 0)):
				arr.remove(j)
	return arr

#sumOfPrimes : loops through primes and sums them
def sumOfPrimes(n):
        if(n < 2):
                return 0;
        else:
                count = 2;
                for i in range(3, n+1):
                        for j in range(2, math.ceil(math.sqrt(i+1)) + 1):
                                if i%j == 0:
                                        break;
                                elif j == math.ceil(math.sqrt(i+1)):
                                        print(f"{i} is a prime");
                                        count += i;
                return count;


#sumOfPrimesV2 :
def sumOfPrimesV2(n):
        arr = []
        primes = []
        for i in range(n+1):
                arr.append(i);
                primes.append(2);

        primes[0] = 0;
        primes[1] = 0;

        for i in range(2, n+1, 2):
                if i == 2:
                        primes[i] = 1;
                else:
                        primes[i] = 0;

        for i in range(3, n+1, 2):
                if((primes[i] == 2) and (i < math.ceil(math.sqrt(n)))):
                        primes[i] = 1;
                        for k in range(2, math.ceil(n/i)):
                                primes[k * i] = 0;

        count = 0;
        for i in range(n + 1):
                if(primes[i]):
                        count += arr[i];

        return count;
