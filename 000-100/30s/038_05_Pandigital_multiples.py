"""
## Pandigital multiples
Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?


Link: https://projecteuler.net/problem=38

Date solved:  
2022/07/05
"""

ANSWER = 932718654

# imports


# solution


def create_pandigital(n):
    digits = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

    sn = ""  # Here is our pandigital number
    i = 1
    while digits:
        # make the pandigital number
        strint = str(n * i)
        sn += strint
        try:
            for char in strint:
                # try and remove each character from the set
                # if it fails, then we don't have a pandigital number
                digits.remove(char)
        except:
            return False, int(sn)
        i += 1
    return True, int(sn)


def solution(bypass=True):
    if bypass:
        return ANSWER

    max_pandigital = 0
    for n in range(10000):
        passes, new_pandigital = create_pandigital(n)
        if passes:
            max_pandigital = max(max_pandigital, new_pandigital)

    return max_pandigital


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer =", ANSWER)
