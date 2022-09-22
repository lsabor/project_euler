"""
## Longest Collatz sequence

Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting 
numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.


Link: https://projecteuler.net/problem=14

Date solved:  
2022/03/08

Co-solved with Andrew Roberts  
Github: @ajroberts0417
"""

ANSWER = 837799

# imports


# solution


def collatz(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1


def find_longest_collatz(threshold):

    already_found = dict()
    longest = 0
    length = 0
    for starting in list(range(2, threshold)):
        n = starting
        current_length = 0
        newly_found = []
        while n != 1:
            if n in already_found:
                current_length += already_found[n]
                break
            newly_found.append(n)
            current_length += 1
            n = collatz(n)

        vallen = current_length
        for found in newly_found:
            already_found[found] = vallen
            vallen -= 1
        if current_length > length:
            length = current_length
            longest = starting

    return longest


def solution(bypass=False):
    if bypass:
        return ANSWER

    return find_longest_collatz(1000000)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
