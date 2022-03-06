# This module holds basic math functions

from numpy import iterable


def sum_consecutive_ints(n: int) -> int:
    # returns sum of consecutive ints up to and including n
    return int(n*(n+1)/2)

def sum_squares(n_list: list) -> float:
    return sum([x**2 for x in n_list])

def iterable_product(iter: iterable) -> float:
    ip = 1
    for n in iter:
        ip *= n
    return ip