# This module holds basic sequence functions

import sequences
import primes
import maths
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
        return primes.prime_factorization(next_tri_num)
    def next_item_batch(self):
        return [self.next_item()]


class Divisor_Sum_Natural_Numbers(sequences.Sequence):
    # lists the sum of the divisors of the natural numbers in order
    def __init__(self,n=1):
        self.name = prefix + 'Divisor_Sum_Natural_Numbers'
        self.starter_seq = [1]
        super().__init__(n)
    def next_item(self):
        next_natural_num = sequences.Natural()[len(self.seq)]
        return sum(maths.divisors(next_natural_num))
    def next_item_batch(self):
        return [self.next_item()]


class Proper_Divisor_Sum_Natural_Numbers(sequences.Sequence):
    # lists the sum of the divisors of the natural numbers in order
    def __init__(self,n=1):
        self.name = prefix + 'Proper_Divisor_Sum_Natural_Numbers'
        self.starter_seq = [1]
        super().__init__(n)
    def next_item(self):
        next_natural_num = sequences.Natural()[len(self.seq)]
        return sum(maths.proper_divisors(next_natural_num))
    def next_item_batch(self):
        return [self.next_item()]