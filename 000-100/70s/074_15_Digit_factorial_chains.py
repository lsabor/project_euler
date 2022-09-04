"""
## Digit factorial chains
Problem 74

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145  

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169  
871 → 45361 → 871  
872 → 45362 → 872  

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)  
78 → 45360 → 871 → 45361 (→ 871)  
540 → 145 (→ 145)  

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

Link: https://projecteuler.net/problem=73

Date solved:  
2022/08/17
"""

ANSWER = 402

# imports

from maths.math import factorial

# solution

# for each n < 1e6,
factorials = [factorial(n) for n in range(10)]  # to avoid recomputing

threshold = int(1e6)


def digit_factorial_sum(n):
    return sum([factorials[int(char)] for char in str(n)])


def digit_factorial_chains(threshold, length):

    # for memoization
    seen = dict()

    count = 0
    for n in range(threshold):
        this_trip = []
        current = n
        while current not in seen:
            # check if we have a new loop that hasn't been seen before
            # if so, then add this loop's info to seen, and break
            if current in this_trip:
                for index, value in enumerate(this_trip[::-1]):
                    seen[value] = index + 1
                this_trip = []
                break
            this_trip.append(current)
            current = digit_factorial_sum(current)
        chain_len = len(this_trip) + seen[current]
        count += chain_len == length
        # momoizing here
        for index, value in enumerate(this_trip):
            seen[value] = chain_len - index

    return count


def solution(bypass=True):
    if bypass:
        return ANSWER

    return digit_factorial_chains(threshold, 60)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
