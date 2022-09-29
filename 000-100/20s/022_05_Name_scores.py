"""
## Names scores

Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?


Link: https://projecteuler.net/problem=22

Date solved:  
2022/04/01
"""

ANSWER = 871198282

# imports


# solution


def solution():
    file_name = "problem_files/p022_names.txt"
    with open(file_name, "r") as f:
        names = f.read()
    names = names[1:-1].split('","')
    names.sort()

    def name_score(name):
        score = 0
        for char in name:
            score += ord(char) - 64
        return score

    name_score_sum = 0
    for i, name in enumerate(names):
        name_score_sum += name_score(name) * (i + 1)

    return name_score_sum


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
