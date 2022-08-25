"""
## Number spiral diagonals
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25  
20 _7 _8 _9 10  
19 _6 _1 _2 11  
18 _5 _4 _3 12  
17 16 15 14 13  

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


Link: https://projecteuler.net/problem=28

Date solved:  
2022/04/24
"""

ANSWER = 669171001

# imports


# solution


def solution(bypass=True):
    if bypass:
        return ANSWER
    dim = 1001

    diagonal_sum = 1
    # start with center number = 1

    num = 1
    # this is the number we are on

    interval = 2
    # this is the distance between diagonal numbers
    # center bit = 1
    # next ring = _ + 3 + _ + 5 + _ + 7  + _ + 9
    # the interval increases by 2 each time we go to the next ring
    # next ring = _ + _ + _ + 13 _ + _ + _ + 17 _ + _ + _ + 21 _ + _ + _ + 25

    last_number = dim**2
    # the numbers in the box are range(1,last_number)

    while num < last_number:  # we skip 1 since we start with 1 already in diagonal_sum
        for i in range(4):  # loop 4 times on this level, once for each corner value
            num += interval
            diagonal_sum += num
        interval += 2

    return diagonal_sum


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer =", ANSWER)
