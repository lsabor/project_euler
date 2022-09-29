"""
## Counting Sundays

Problem 19

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?



Link: https://projecteuler.net/problem=19

Date solved:  
2022/03/21
"""

ANSWER = 171

# imports


# solution


def isLeapYear(year: int) -> bool:
    if year % 100 == 0:  # year is a century year
        if year % 400 == 0:  # year is a centry year divisible by 400
            return True  # is a leap year
        return False  # isn't a leap year
    if year % 4 == 0:
        return True  # is a leap year
    return False  # isn't a leap year


def monLen(month: int, year: int) -> int:
    if month in [0, 2, 4, 6, 7, 9, 11]:
        return 31
    elif month == 1:
        return 29 if isLeapYear(year) else 28
    return 30


def solution():
    # find day of week Jan 1 1901
    len_1900 = 366 if isLeapYear(1900) else 365
    jan1_1901_day_of_week = (len_1900 + 1) % 7  # 0: Sunday, 1: Monday, ...

    sundays_on_first = 0  # our counter
    day_of_week = jan1_1901_day_of_week  # starting point
    for year in range(1901, 2001):
        for month in range(0, 12):
            for day in range(0, monLen(month, year)):
                if day == 0 and day_of_week == 0:
                    sundays_on_first += 1
                day_of_week = (day_of_week + 1) % 7

    return sundays_on_first


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
