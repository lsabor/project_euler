"""
## Spiral primes
Problem 58

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31  
38 17 16 15 14 13 30  
39 18 _5 _4 _3 12 29  
40 19 _6 _1 _2 11 28  
41 20 _7 _8 _9 10 27  
42 21 22 23 24 25 26  
43 44 45 46 47 48 49  

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

Link: https://projecteuler.net/problem=58

Date solved:  
2022/07/25
"""

# TODO: refactor for speed

ANSWER = 26241

# imports

from maths.primes import isPrime


# solution

threshold = 0.1


def find_diminishing_prime_threshold():
    diagonal_number_count = 1
    prime_diagonal_number_count = 0

    num = 1
    interval = 2

    while True:
        # for _ in range(4):
        new_diag_nums = []
        for _ in range(4):
            num += interval
            new_diag_nums.append(num)
        diagonal_number_count += 4
        for n in new_diag_nums:
            prime_diagonal_number_count += isPrime(n)
        if prime_diagonal_number_count / diagonal_number_count < threshold:
            return interval + 1

        interval += 2


def solution(bypass=False):
    if bypass:
        return ANSWER

    return find_diminishing_prime_threshold()


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
