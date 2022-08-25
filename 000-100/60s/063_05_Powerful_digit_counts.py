"""
## Powerful digit counts
Problem 63

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

Link: https://projecteuler.net/problem=63

Date solved:  
2022/07/29
"""

ANSWER = 49

# imports


# solution


def countPowerfulDigits():
    count = 0
    for n in range(1, 10):
        p = 1
        while len(str(n**p)) == p:
            count += 1
            p += 1
    return count


def solution(bypass=True):
    if bypass:
        return ANSWER

    return countPowerfulDigits()


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer =", ANSWER)
