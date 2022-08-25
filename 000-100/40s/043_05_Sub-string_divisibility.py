"""
## Sub-string divisibility
Problem 43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.



Link: https://projecteuler.net/problem=43

Date solved:  
2022/07/07
"""

ANSWER = 16695334890

# imports


# solution


"""
define dn to be nth digit in pandigital d
rules:
1)  d2d3d4 is divisible by 2
2)  d3d4d5 is divisible by 3
3)  d4d5d6 is divisible by 5
4)  d5d6d7 is divisible by 7
5)  d6d7d8 is divisible by 11
6)  d7d8d9 is divisible by 13
7)  d8d9d10 is divisible by 17

8)  by 1) d4 in [0, 2, 4, 6, 8]
9)  by 2) d3 + d4 + d5 is divisible by 3
10) by 3) d6 in [0, 5]
11) by 4) d5d6 - 2*d7 is divisible by 7
12) by 5) d7-d6-d8 in [-11,0,11]
13) by 6) (d7d8 + 4*d9) divisible by 13
14) by 7) (d8d9 - 5*d10) divisible by 17

15) by 10) & 11) d6 == 0 -> (d5, d7) in [(1,5),(2,3),(3,[1,8]),(4,6),(5,4),(6,[2,9]),(8,5),(9,3)]
15) by 10) & 11) d6 == 5 -> (d5, d7) in [(0,6),(1,4),(2,9),(3,[0,7]),(6,[1,8]),(7,6),(8,4),(9,2)]

"""


def get_pandigital(*args):
    ex = 9
    pandigital = 0
    for d in args:
        pandigital += d * (10**ex)
        ex -= 1
    return pandigital


def solution(bypass=False):
    if bypass:
        return ANSWER

    d = set(range(10))

    valid_pandigitals = []

    for d6 in [0, 5]:
        d.remove(d6)
        if d6 == 0:
            d5d7 = [(1, 5), (2, 3), (3, [1, 8]), (4, 6), (5, 4), (6, [2, 9]), (8, 5), (9, 3)]
        if d6 == 5:
            d5d7 = [(0, 6), (1, 4), (2, 9), (3, [0, 7]), (6, [1, 8]), (7, 6), (8, 4), (9, 2)]
        for d5, d7s in d5d7:
            d.remove(d5)
            if type(d7s) == int:
                d7s = [d7s]
            for d7 in d7s:
                d.remove(d7)
                for d4 in list(d):
                    if d4 % 2 == 0:
                        d.remove(d4)
                        for d3 in list(d):
                            if sum([d3, d4, d5]) % 3 == 0:
                                d.remove(d3)
                                for d8 in list(d):
                                    if d7 - d6 - d8 in set([-11, 0, 11]):
                                        d.remove(d8)
                                        for d9 in list(d):
                                            if (10 * d7 + d8 + 4 * d9) % 13 == 0:
                                                d.remove(d9)
                                                for d10 in list(d):
                                                    if (10 * d8 + d9 - 5 * d10) % 17 == 0:
                                                        d.remove(d10)
                                                        for d2 in list(d):
                                                            d.remove(d2)
                                                            for d1 in list(d):
                                                                if d1 != 0:
                                                                    valid_pandigitals.append(
                                                                        get_pandigital(
                                                                            d1,
                                                                            d2,
                                                                            d3,
                                                                            d4,
                                                                            d5,
                                                                            d6,
                                                                            d7,
                                                                            d8,
                                                                            d9,
                                                                            d10,
                                                                        )
                                                                    )
                                                            d.add(d2)
                                                        d.add(d10)
                                                d.add(d9)
                                        d.add(d8)
                                d.add(d3)
                        d.add(d4)
                d.add(d7)
            d.add(d5)
        d.add(d6)

    return sum(valid_pandigitals)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
