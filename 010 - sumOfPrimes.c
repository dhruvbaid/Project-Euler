#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* Implementation 1: every number i < n is iterated through, and whether it is
 * prime or not is determined based on checking the remainders when dividing it
 * by all numbers 2 <= j <= ceil(sqrt(i+1)) + 1
 */
unsigned long long int sumOfPrimes(unsigned int n)
{
    if(n < 2)
    {
	return 0;
    }
    else
    {
	unsigned long long int count = 0;
	for(unsigned int i = 2; i < n; i++)
	{
	    if((i == 2) || (i == 3))
	    {
		count += i;
	    }
	    else
	    {
		for(int j = 2; j < ceil(sqrt((double)(i + 1))) + 1; j++)
		{
		    // checking all factors between 2 and sqrt(i) inclusive
		    if(i % j == 0)
		    {
			break;
		    }
		    else if(j == floor(sqrt((double)(i + 1))))
		    {
			count += i;
		    }
		}
	    }
	}
	return count;
    }
}

/* Implementation 2: use the modified Sieve of Eratosthenes and create a new
 * array which contains the booleans representing whether the original number
 * is prime or not
 */
unsigned long long int sumOfPrimesv2(unsigned int n)
{
    unsigned int* arr = (unsigned int*)malloc((n + 1) * sizeof(int));
    for(unsigned int i = 0; i < n + 1; i++)
    {
	arr[i] = i;
    }
    // arr contains all the numbers from 0 to n inclusive

    unsigned char* primes = (unsigned char*)malloc((n + 1) * sizeof(char));
    for(unsigned int i = 0; i < n + 1; i++)
    {
	primes[i] = 2;
	// allocate a placeholder value temporarily
    }
    
    primes[0] = 0;
    // 0 is not a prime
    primes[1] = 0;
    // 1 is not a prime
    
    for(unsigned int i = 2; i < n + 1; i += 2)
    {
	if(i == 2)
	{
	    // 2 is the only even prime
	    primes[i] = 1;
	}
	else
	{
	    // all primes larger than 2 are marked as composite
	    primes[i] = 0;
	}
    }

    for(unsigned int i = 3; i < n + 1; i += 2)
    {
	// iterate through all odd numbers >= 3 and use the sieve to test if
	// they are prime or not
	if((primes[i] == 2) && (i < ceil(sqrt((double)n))))
	{
	    primes[i] = 1;
	    for(unsigned int k = 2; k < (n / i) + 1; k++)
	    {
		primes[k * i] = 0;
	    }
	}
    }

    unsigned long long int count = 0;

    for(unsigned int i = 0; i < n + 1; i++)
    {
	// loop through primes array and use those indices to add values from
	// original arr array which contains the actual numbers
	if(primes[i])
	{
	    count += arr[i];
	}
    }

    free(arr);
    free(primes);

    return count;
}

int main(int argc, char* argv[])
{
    unsigned int n = atoi(argv[1]);
    // printf("Sum of primes less than %u = %lld\n", n, sumOfPrimes(n));
    printf("Sum of primes less than %u = %lld\n", n, sumOfPrimesv2(n));
}
