"""
## Coin sums
Problem 31

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?



Link: https://projecteuler.net/problem=31

Date solved:  
2022/05/28
"""

ANSWER = 73682

# imports


# solution

coins = [1, 2, 5, 10, 20, 50, 100, 200]  # must be ascending


def ways_to_compose(n):
    matrix = [[1] + [0] * n]
    for row, coin in enumerate(coins):
        new_methods = []
        for amount in range(n + 1):
            wo_new = matrix[row][amount]
            w_new = (
                0 if coin > len(new_methods) else new_methods[len(new_methods) - coin]
            )
            new_methods.append(wo_new + w_new)
        matrix.append(new_methods)

    return matrix[-1][-1]


def solution(bypass=True):
    if bypass:
        return ANSWER
    return ways_to_compose(200)


if __name__ == "__main__":
    solution(bypass=False)
