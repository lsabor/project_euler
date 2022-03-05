# This module holds basic math functions

def sum_consecutive_ints(n: int) -> int:
    # returns sum of consecutive ints up to and including n
    return int(n*(n+1)/2)