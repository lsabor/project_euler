"""
## Totient maximum

Problem 69

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of  
numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine  
and relatively prime to nine, φ(9)=6.  
n 	....Relatively Prime 	                ....φ(n)   .. n/φ(n)  
2 	....1 	..................................1 .......	2  
3 	....1,2 	 ...............................2 .......	1.5  
4 	....1,3 	 ...............................2 .......	2  
5 	....1,2,3,4      .........................4 .......	1.25  
6 	....1,5 	 ...............................2 .......	3  
7 	....1,2,3,4,5,6 	       .................6 .......	1.1666...  
8 	....1,3,5,7 	    ........................4 .......	2  
9 	....1,2,4,5,7,8 	       .................6 .......	1.5  
10 	..1,3,7,9 	       .......................4 .......	2.5  

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.



Link: https://projecteuler.net/problem=69

Date solved:  
2022/08/06
"""

ANSWER = 510510

# imports

from maths.sequences import PrimesSeq

# solution


def solution(bypass=False):
    if bypass:
        return ANSWER

    # the ratio n / phi(n) will be largest when n is big and phi(n) is small
    # phi(n) is invesely proportional to number of factors
    # thus, we find the largest number below 1e6, that has the most factors
    # we can generate that number by finding the largest product of the lowest primes below 1e6
    ps = PrimesSeq()
    n = 1
    for p in ps:
        n *= p
        if n > 1e6:
            n /= p
            return int(n)
            break


if __name__ == "__main__":
    solution(bypass=False)
