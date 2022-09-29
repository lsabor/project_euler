"""
## Truncatable primes

Problem 37

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


Link: https://projecteuler.net/problem=37

Date solved:  
2022/06/29
"""

ANSWER = 748317

# imports

from maths.sequences import PrimesSeq

# solution


P = PrimesSeq()
p_list = P.seq
p_set = P.set()


def is_left_truncated_prime(p):
    if p < 10:
        return p in set((2, 3, 5, 7))
    else:
        truncated = int(str(p)[1:])
        if truncated in p_set:
            return is_left_truncated_prime(truncated)
        else:
            return False


def is_right_truncated_prime(p):
    if p < 10:
        return p in set((2, 3, 5, 7))
    else:
        truncated = int(str(p)[:-1])
        if truncated in p_set:
            return is_right_truncated_prime(truncated)
        else:
            return False


def solution():

    double_truncated_primes = []
    double_truncated_primes_count = 0
    for p in p_list[4:]:
        if is_left_truncated_prime(p) and is_right_truncated_prime(p):
            double_truncated_primes.append(p)
            double_truncated_primes_count += 1
        if double_truncated_primes_count == 11:
            break

    return sum(double_truncated_primes)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
