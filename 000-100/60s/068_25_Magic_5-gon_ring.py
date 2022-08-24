"""
## Magic 5-gon ring
Problem 68

Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

SEE IMAGE AT URL

Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.  
Total	Solution Set  
09	4,2,3; 5,3,1; 6,1,2  
09	4,3,2; 6,2,1; 5,1,3  
10	2,3,5; 4,5,1; 6,1,3  
10	2,5,3; 6,3,1; 4,1,5  
11	1,4,6; 3,6,2; 5,2,4  
11	1,6,4; 5,4,2; 3,2,6  
12	1,5,6; 2,6,4; 3,4,5  
12	1,6,5; 3,5,4; 2,4,6  

By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?

SEE IMAGE AT URL


Link: https://projecteuler.net/problem=68

Date solved:  
2022/08/06
"""

ANSWER = 6531031914842725

# imports


# solution


def solution(bypass=True):
    if bypass:
        return ANSWER

    # objective is to maximize strint = "AabBbcCcdDdeEea" such that:
    # 1) S == A+a+b == B+b+c == C+c+d == D+d+e == E+e+a
    # 2) A == min([A,B,C,D,E])
    # 3) 10 in set([B,C,D,E]) # since len(strint)==16
    # 4) set([A,a,B,b,D,d,E,e]) == set(range(1,11))

    # first let's try to build the largest possible strint
    A = 6  # assume A is the smallest external number - assume Alpha = set([A,B,C,D,E]) == set(range(6,11))
    a = 5  # assume a is the largest internal number - assume beta = set([a,b,c,d,e]) == set(range(1,6))
    # implies large numbers on outside, small numbers on inside
    S = 14  # since S = S0 / 5 = (sum(Alpha) + 2*sum(Beta)) / 5 = 70 / 5 = 14
    b = 3  # so that A + a + b = 11 + b == 14
    # thus {B,D} == {8,10} and {C,E} == {7,9} since B+D == C+E+2
    e = 2  # since E + e == 9, and if E==9, e == 0 which would be a contradiction
    E = 7
    C = 9
    B = 10  # since B + c == 11 and B is even and c is either 1 or 4
    c = 1
    D = 8  # last large number
    d = 4  # last small number

    # verify assumptions
    # assumption 1)
    assert S == A + a + b == B + b + c == C + c + d == D + d + e == E + e + a
    # assumption 2)
    assert A == min([A, B, C, D, E])
    # assumption 3)
    assert 10 in set([B, C, D, E])
    # assumption 4)
    assert set([A, a, B, b, C, c, D, d, E, e]) == set(range(1, 11))

    # since:
    # 1) A and a are as large as possible
    # 2) all other numbers were deduced and could not be any other way
    # 3) all assumptions pass to ensure solution is in fact a Magic 5-gon ring
    # then we have found the largest possible strint
    sol = [A, a, b, B, b, c, C, c, d, D, d, e, E, e, a]
    return int("".join(map(str, sol)))


if __name__ == "__main__":
    solution(bypass=False)
