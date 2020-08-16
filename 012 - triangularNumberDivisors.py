"""
Highly Divisible Triangular Number: What is the value of the first triangular
number to have over five hundred divisors?
"""
import math

def triangular(n):
        numFac = 0;
        i = 1;
        while(numFac < n):
                arr = []
                tNum = int((i * (i+1))/2);
                for f in range(1, math.floor(math.sqrt(tNum)) + 1):
                        if(tNum%f == 0):
                                if(f == math.sqrt(tNum)):
                                        arr.append(int(f));
                                else:
                                        arr.append(f);
                                        arr.append(int(tNum / f));
                numFac = len(arr);
                i += 1;
        return tNum;
