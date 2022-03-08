# This module holds basic sequence functions

import sequences
import primes
from collections import Counter

prefix = 'compoud/'

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





