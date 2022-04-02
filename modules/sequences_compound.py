# This module holds basic sequence functions

import sequences
from primes import prime_factorization
from maths import divisors_from_pf_counter
from collections import Counter

prefix = 'compound/'

class Triangle_Numbers_Prime_Factorization(sequences.Sequence):
    # lists the triangle numbers in order
    # Nth triangle num is sum of all natural numbers up to N
    def __init__(self,n=1):
        self.name = prefix + 'Triangle_Numbers_Prime_Factorization'
        self.starter_seq = [Counter([1])]
        super().__init__(n)
    def next_item(self):
        next_tri_num = sequences.Triangle_Numbers()[len(self.seq)]
        return prime_factorization(next_tri_num)
    def next_item_batch(self):
        return [self.next_item()]


class Divisors_Positive_Integers(sequences.Sequence):
    # lists the Divisors in list form of the natural numbers in order
    def __init__(self,n=1):
        self.name = prefix + 'Divisors_Positive_Integers'
        self.starter_seq = [[0],[1]]
        super().__init__(n)
    def next_item(self):
        return self.next_item_batch[0]
    def next_item_batch(self):
        length = len(self)
        next_items = []
        PF = sequences.Prime_Factorizations()
        for i in range(length,length*2 + 1):
            next_items.append(divisors_from_pf_counter(PF[i]))
        return next_items



class Proper_Divisor_Sum_Positive_Integers(sequences.Sequence):
    # lists the sum of the divisors of the natural numbers in order
    def __init__(self,n=1):
        self.name = prefix + 'Proper_Divisor_Sum_Positive_Integers'
        self.starter_seq = [0,0]
        super().__init__(n)
    def next_item(self):
        return sum(Divisors_Positive_Integers()[len(self)][:-1])
    def next_item_batch(self):
        return [self.next_item()]

    def next_item(self):
        return self.next_item_batch[0]
    def next_item_batch(self):
        length = len(self)
        next_items = []
        D = Divisors_Positive_Integers()
        for i in range(length,length*2 + 1):
            next_items.append(sum(D[i][:-1]))
        return next_items