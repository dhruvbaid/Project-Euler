"""
Largest product in a series: Find the thirteen adjacent digits in the 1000-digit
number that have the greatest product. What is the value of this product?
"""

# maxProd : finds maximum product of k adjacent digits in a number n
def maxProd(n, k):
    s = f"{n}";
    if(len(s) < k):
        return -1;
    else:
        arr = []
        newArr = [];
        for i in range(0, len(s) - k + 1):
            arr.append(s[i:i+k]);
        for x in arr:
            p = 1;
            for j in x:
                p *= int(j);
            newArr.append(p)
        newArr.sort();
        return newArr[-1];
