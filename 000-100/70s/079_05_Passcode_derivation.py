"""
Passcode derivation

Problem 79

A common security method used for online banking is to ask the user for three random 
characters from a passcode. For example, if the passcode was 531278, they may ask for 
the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as 
to determine the shortest possible secret passcode of unknown length.


Link: https://projecteuler.net/problem=79

Date solved:  
09/13/2022
"""

ANSWER = 73162890

# imports


# solution

file_name = "problem_files/p079_keylog.txt"
with open(file_name, "r") as f:
    keylog = f.read()
keylog = keylog.split("\n")
keylog = [[int(c) for c in key] for key in keylog]


def get_logs(keylog):
    logs = []

    for n in range(10):
        befores = set()
        afters = set()
        for key in keylog:
            if n in key:
                index = key.index(n)
                befores = befores.union(set(key[:index]))
                if index != len(key) - 1:
                    afters = afters.union(set(key[index + 1 :]))
        if befores or afters:
            logs.append([befores, afters, n])
    return logs


def solution():

    logs = get_logs(keylog)
    logs.sort(key=lambda x: len(x[0]))

    number = []
    for digit in logs:
        number.append(str(digit[2]))

    return int("".join(number))


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
