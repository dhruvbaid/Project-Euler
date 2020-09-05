"""
Coded triangle numbers: The nth term of the sequence of triangle numbers is
given by, tn = n(n+1)/2; so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
"""
import math

def isTriangle(word: str):
    val = 0
    word = word.upper()
    for letter in word:
        v = ord(letter)
        if 65 <= v <= 90:
            val += ord(letter) - 64
        else:
            return False
    for n in range(1, math.ceil(math.sqrt(2*val)) + 1):
        if val == n*(n+1)/2:
            return True
    return False

def main():
    count = 0
    with open("042_input.txt") as f:
        a = f.read().split(",")
    for word in a:
        if isTriangle(word[1:-1]):
            count += 1
    return count
