"""
Lychrel Numbers: if we take a number, reverse it, and add the two, we obtian a
new number. If we do this repeatedly, sometimes, we end up with a palindrome. If
we can never obtain a palindrome, however, the original number is called a
Lychrel Number. How many Lychrel Numbers are there below 10,000?

Assumptions:
    1. It will not take more than 50 iterations to obtain a palindrome IF the
       number is not Lychrel.
    2. Palindromic numbers are not automatically non-Lychrel; they have to be
       iterated as well.
"""

# isPalindrome : checks if a number is palindromic
def isPalindrome(x: int) -> bool:
    xStr = str(x)
    for i in range(int(len(xStr)/2)):
        if xStr[i] != xStr[len(xStr) - 1 - i]:
            return False
    return True

# reverse : reverses a given number and returns the new integer
def reverse(x: int) -> int:
    xStr = str(x)
    rev = int(xStr[::-1])
    return rev

# main : returns the number of Lychrel Numbers from 1 to maxNum (inclusive)
def main(maxNum: int) -> int:
    lychrel = []
    for num in range(1, maxNum + 1):
        iterated = num + reverse(num)
        for iteration in range(50):
            if isPalindrome(iterated):
                break
            elif iteration == 49:
                lychrel.append(num)
                break
            else:
                iterated += reverse(iterated)
    return len(lychrel)
