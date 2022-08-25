"""
## 1000-digit Fibonacci number
Problem 25

The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?



Link: https://projecteuler.net/problem=25

Date solved:  
2022/04/10
"""

# TODO: refactor for speed

ANSWER = 4782

# imports


# solution


def add_strints(n1, n2):
    # TODO: make a strints module
    # strint is a backwards string rep of an int: "123" == 321
    # n1 < n2
    remainder = 0
    result = ""
    for i, I2 in enumerate(n2):
        if len(n1) > i:
            I1 = n1[i]
        else:
            I1 = "0"
        newint = int(I1) + int(I2) + remainder
        remainder = newint // 10
        newstrint = str(newint % 10)
        result += newstrint
    if remainder:
        result += str(remainder)
    return result


def solution(bypass=True):
    if bypass:
        return ANSWER
    n1 = "1"
    n2 = "1"
    index = 2

    threshold = 1000

    while len(n2) < threshold:
        new = add_strints(n1, n2)
        n1 = n2
        n2 = new
        index += 1

    return index


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
