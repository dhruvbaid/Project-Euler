#include <stdio.h>
#include <stdlib.h>

unsigned int count(unsigned int* nums, unsigned int x, unsigned int n)
{
    unsigned int res = 0;
    for(unsigned int i = 0; i < n; i++)
    {
	if(nums[i] == x)
	{
	    res++;
	}
    }
    return res;
}

void append(unsigned int** list, unsigned int* numFactors, unsigned int x)
{
    unsigned int* old = *list;
    unsigned int* res = (unsigned int*)malloc(((*numFactors) + 1) * sizeof(unsigned int));
    res[*numFactors] = x;
    if(*numFactors > 0)
    {
	for(unsigned int i = 0; i < *numFactors; i++)
	{
	    res[i] = old[i];
	}
    }
    (*numFactors)++;
    *list = res;
    free(old);
}

void pFac(unsigned int** factors, unsigned int* numFactors, unsigned int n)
{
    if(n < 2)
    {
	*numFactors = 0;
    }
    else
    {
	while((n % 2) == 0)
	{
	    append(factors, numFactors, 2);
	    n = n / 2;
	}
	unsigned int i = 3;
	while(n > 1)
	{
	    while((n % i) == 0)
	    {
		append(factors, numFactors, i);
		n = n / i;
	    }
	    i += 2;
	}
	return;
    }
}

unsigned int nthPrime(unsigned int n)
{
    unsigned int res = 2;
    unsigned int i = 0;
    while(i < (n - 1))
    {
	unsigned int currPrime = res;
	unsigned int newPrime = currPrime + 1;

	unsigned int* factors = NULL;
	unsigned int numFactors = 0;
	pFac(&factors, &numFactors, newPrime);

	unsigned int k = factors[0];
	free(factors);

	while(k != newPrime)
	{
	    newPrime++;

	    unsigned int* factors = NULL;
	    numFactors = 0;
	    pFac(&factors, &numFactors, newPrime);
	    k = factors[0];
	    free(factors);
	}

	res = newPrime;
	i++;
    }
    return res;
}

int main(int argc, char* argv[])
{
    unsigned int p = nthPrime(10001);
    printf("Prime number 10001 = %u\n", p);
}
