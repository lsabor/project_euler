"""
## Maximum path sum II

Problem 67

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 2^99 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)



Link: https://projecteuler.net/problem=67

Date solved:  
2022/04/02
"""

ANSWER = 7273

# imports

from maths.parsing import readArrayStr

# solution


def get_longest_path_length(triangle_array):
    triangle_array.reverse()

    previous_row = triangle_array[0]
    for row in triangle_array[1:]:
        for i, value in enumerate(row):
            row[i] = max(value + previous_row[i], value + previous_row[i + 1])
        previous_row = row

    return row[0]


def solution():

    file_name = "problem_files/p067_triangle.txt"
    with open(file_name, "r") as f:
        triangle = f.read()

    triangle_array = readArrayStr(triangle)

    return get_longest_path_length(triangle_array)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
