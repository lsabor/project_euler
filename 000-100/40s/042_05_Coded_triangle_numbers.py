"""
## Coded triangle numbers
Problem 42

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?



Link: https://projecteuler.net/problem=42

Date solved:  
2022/07/06
"""

ANSWER = 162

# imports

from maths.sequences import TriangleNumbers


# solution
T = TriangleNumbers()

file_name = "problem_files/p042_words.txt"
with open(file_name, "r") as f:
    words = f.read()
words = words.replace('"', "").split(",")


def char_val(char):
    return ord(char.upper()) - 64


def word_val(word):
    return sum(map(char_val, word))


def count_triangle_words():
    count = 0
    for word in words:
        if T._isInSetSpecified(word_val(word)):
            count += 1
    return count


def solution():
    return count_triangle_words()


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
