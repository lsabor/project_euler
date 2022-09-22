"""
## Digit fifth powers
Problem 30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


Link: https://projecteuler.net/problem=30

Date solved:  
2022/05/18
"""

# TODO: refactor for speed

ANSWER = 443839

# imports


# solution

# let f(N) = the sum of the 5th power of the decimal based digits of N
def f(N):
    n_string = str(N)
    sum = 0
    for char in n_string:
        digit = int(char)
        fifth_power = digit**5
        sum += fifth_power
    return sum


def get_max_N():
    # find N s.t. for all n>N, f(n) < n.
    N = 9
    while True:
        fn = f(N)
        if fn < N:
            break
        N = 10 * N + 9
    return N


def solution(bypass=False):
    if bypass:
        return ANSWER
    N = get_max_N()  # returns 354294

    digit_fifth_powers = []
    for n in range(2, N + 1):
        if f(n) == n:
            digit_fifth_powers.append(n)

    return sum(digit_fifth_powers)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
