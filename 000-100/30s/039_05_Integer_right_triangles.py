"""
## Integer right triangles
Problem 39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?


Link: https://projecteuler.net/problem=39

Date solved:  
2022/07/06
"""

# TODO: refactor for speed

ANSWER = 840

# imports

from maths.math import sqrt, ceil

# solution

"""
Math:

p = perimeter  
h = hypotenuse  
l = long side  
s = short side  

p = h + l + s  
h > l >= s

maximum possible value of h => s=1 and l=h-1, thus p = h + h-1 + 1 = 2\*h  
max(h) = p/2

minimum possible value of h => l = s = h\*sqrt(2)/2, thus p = h + 2\*h\*sqrt(2)/2 = h + h\*sqrt(2) = h(1 + sqrt(2))  
min(h) = p/(1+sqrt(2))

Thus, our search space starts with only investigating h | p/(1+sqrt(2)) < h <= p/2  
Then, cycle from l=h-1 to l=h*sqrt(2)/2 to find triples
"""

p = 1000


def find_triples(p):
    triples = []

    h_min_value = int(p / (1 + sqrt(2))) + 1
    h_max_value = int(p / 2)

    for h in range(h_min_value, h_max_value + 1):
        # for each h, check for triples across l
        for l in range(ceil(sqrt(2) / 2 * h), h):
            s = p - h - l
            if h**2 == l**2 + s**2:
                triples.append((h, l, s))
    return triples


def solution(bypass=False):
    if bypass:
        return ANSWER

    best_p = 0
    best_count = 0
    for n in range(10, p + 1):
        count = len(find_triples(n))
        if count > best_count:
            best_count = count
            best_p = n

    return best_p


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer =", ANSWER)
