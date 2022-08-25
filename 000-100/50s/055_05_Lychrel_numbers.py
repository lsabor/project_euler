"""
## Lychrel numbers


  [Show HTML problem content]  
Problem 55

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.



Link: https://projecteuler.net/problem=55

Date solved:  
2022/07/28  
w/ George Jeffreys
"""

ANSWER = 249

# imports


# solution

threshold = 10000


def is_lychrel_number(n):

    current = str(n)  # strint

    for _ in range(50):
        new = int(current) + int(current[::-1])

        # see if new is a palindrone
        if str(new) == str(new)[::-1]:
            return False

        current = str(new)

    return True


def count_lychrel_numbers(threshold):
    count = 0

    for n in range(1, threshold):
        if is_lychrel_number(n):
            count += 1

    return count


def solution(bypass=True):
    if bypass:
        return ANSWER

    return count_lychrel_numbers(threshold)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
