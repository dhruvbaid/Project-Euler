"""
Digital Fifth Powers: Find the sum of all the numbers that can be written as the
sum of fifth powers of their digits.
"""

def digPowers():
    arr = []
    for i in range(1, 999999):
        s = f"{i}"
        count = 0
        for x in s:
            count += pow(int(x), 5)
        if count == i:
            arr.append(i)
    print(arr)
