"""
Longest Collatz Sequence - Which starting number, under one million, produces
the longest collatz sequence?
"""

def longestSeq(n):
        seqLen = [];
        maxCount = 1;
        maxInt = 1;
        for i in range(n):
                seqLen.append(0);
        for i in range(1, n+1):
                curr = i;
                count = 1;
                while(curr != 1):
                        if(curr < i):
                                count += seqLen[curr - 1];
                                break;
                        if(curr % 2 == 0):
                                curr = int(curr / 2);
                        else:
                                curr = (3 * curr) + 1;
                        count += 1;
                seqLen[i - 1] = count;
                if count > maxCount:
                        maxCount = count;
                        maxInt = i;
        return maxInt;
