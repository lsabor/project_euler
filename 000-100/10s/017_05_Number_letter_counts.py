"""
## Number letter counts

Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


Link: https://projecteuler.net/problem=17

Date solved:  
2022/03/06

Co-solved with Andrew Roberts  
Github: @ajroberts0417
"""

ANSWER = 21124

# imports


# solution

ones_dict = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    101: "and",
    1000: "onethousand",
}

length_dict = {}

for key, value in ones_dict.items():
    length = len(value)
    length_dict[key] = length


def solution():
    total_length = length_dict[1000]  # 'THOUSAND'
    for i in range(1, 1000):
        last_two = i % 100
        if i > 99:
            total_length += length_dict[100]  # 'HUNDRED'
            if last_two % 100 != 0:
                total_length += length_dict[101]  # 'AND'
        total_length += length_dict[i // 100]  # 'ONE'-hundred
        if last_two < 20:
            total_length += length_dict[last_two]  # 'ONE' -> ''NINETEEN'
        else:
            ones = last_two % 10
            total_length += length_dict[ones]  # 'ONE' -> 'NINE
            tens = last_two // 10 * 10
            total_length += length_dict[tens]  # 'TEN' -> 'NINETY'
    return total_length


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
