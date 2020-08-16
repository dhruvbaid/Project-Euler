"""
Large Sum - find the first 10 digits of the sum of the 100 50-digit numbers in
the input file
"""
import math

def readFile(file):
        arr = []
        with open(file) as f:
                a = f.readlines();
        for x in a:
                if(x == a[-1]):
                        print(int(x));
                        arr.append(int(x));
                else:
                        print(int(x[0:-1]));
                        arr.append(int(x[0:-1]))
        return arr;

def summation(arr):
        count = 0;
        for x in arr:
                count += x / (10 ** 49);
        s = f"{count}"
        return s[0:11];

def bigSum():
        arr = readFile('013_input.txt');
        s = summation(arr);
        print(s);
