"""
## Largest prime factor

Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?



Link: https://projecteuler.net/problem=3

Date solved:  
2022/03/05
"""

ANSWER = 906609

# imports


# solution


def isPalandrome(n: int) -> bool:
    s = str(n)
    return s == s[::-1]


def largePalindromes():
    palindroms = []
    i = j = 999
    while i >= 100:
        while j >= i:
            n = i * j
            if isPalandrome(n):
                palindroms.append(n)
            j -= 1
        j = 999
        i -= 1
    return palindroms


def solution():
    return max(largePalindromes())


if __name__ == "__main__":
    solution()
