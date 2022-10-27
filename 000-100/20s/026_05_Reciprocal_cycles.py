"""
## Reciprocal cycles
Problem 26

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.




Link: https://projecteuler.net/problem=26

Date solved:  
2022/04/10
"""

# TODO: refactor for speed

ANSWER = 983

# imports


# solution


def longest_cycle(n):
    seen_values = []
    result = []
    remainder = 10
    while True:
        quotient = remainder // n
        result.append(quotient)
        new_remainder = remainder % n
        if new_remainder in seen_values:
            break
        seen_values.append(new_remainder)
        remainder = new_remainder * 10
    return result


def solution():
    search_space = 1000

    longest = 0
    long_cycle = []
    for n in range(1, search_space):
        cycle = longest_cycle(n)
        length = len(cycle)
        if len(cycle) > longest:
            longest = length
            long_cycle = cycle

    return longest


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
