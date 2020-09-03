"""
Reciprocal Cycles: Find the value of d < 1000 for which 1/d contains the longest
recurring cycle in its decimal fraction part.
"""
import math

def main():
    d = {1:0}
    for i in range(2, 1000):
        if 2<=i<=10:
            n = str(1/i)[2:]
        elif 11<=i<=100:
            n = str(1/i)[3:]
        else:
            n = str(1/i)[4:]

        if len(n) > 7:
            # 1/i has a non-terminating decimal part
            # print(f"1/{i} = {n}")
            for j in range(1, math.ceil(len(n)/2) + 2):
                # check for repeating pattern of length j
                for start in range(math.ceil(len(n)/2)):
                    # check from index start
                    sub = n[start:start+j+1]
                    if n[start+j+1:].find(sub) == 0:
                        d[i] = j

    print(d)
    m = max(list(d.values()))
    for x in list(d.items()):
        if x[1] == m:
            print(f"1/{x[0]} = {1/x[0]}")
