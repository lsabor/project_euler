# This module holds basic sequence functions

import json
import os
import itertools

class Sequence:
    display_len = 10

    def __init__(self,n: int):
        self.cache_file = '../caches/sequences/'+self.name+'.json'
        self.read_cache()
        if len(self.seq) < n:
            self.extend_seq(n-len(self.seq))

    def reset(self):
        self.seq = self.starter_seq
        self.update_cache()

    def read_cache(self):
        # initilizes self.seq
        if os.path.exists(self.cache_file):
            with open(self.cache_file,'r') as cache:
                self.seq = json.load(cache)
        else:
            self.seq = self.starter_seq
            self.update_cache()
        
    def update_cache(self):
        with open(self.cache_file,'w') as cache:
            cache.write(json.dumps(self.seq))

    def __repr__(self):
        if len(self) < Sequence.display_len:
            return str(self.seq) 
        return str(self.seq[:Sequence.display_len])

    def __getitem__(self,index):
        length = len(self.seq)
        if index < length:
            return self.seq[index]
        else:
            self.extend_seq(index-length+1)
            return self.seq[index]

    def __len__(self):
        return len(self.seq)

    def display(self):
        print(self.seq)

    def next(self):
        return self.next_item()

    def add_item(self):
        nxt = self.next()
        self.seq.append(nxt)
        self.update_cache()
        return nxt

    def extend_seq(self,n: int):
        for i in range(n):
            self.add_item()
        return self

    def take_while(self,include_condition,last_index=1000) -> list:
        passing = []
        length = 0
        while length < last_index:
            new_item = self[length]
            if include_condition(new_item):
                passing.append(new_item)
                length += 1
            else:
                return passing
        raise Exception(f'Sequence {self.name} satisfies {include_condition} past {last_index=}')

    def take_while_lt(self,n: float) -> list:
        return self.take_while(lambda x: x< n)
    def take_while_gt(self,n: float) -> list:
        return self.take_while(lambda x: x> n)
    def take_while_le(self,n: float) -> list:
        return self.take_while(lambda x: x<=n)
    def take_while_ge(self,n: float) -> list:
        return self.take_while(lambda x: x>=n)

class Primes(Sequence):
    def __init__(self,n=1):
        self.name = 'primes'
        self.starter_seq = [2]
        super().__init__(n)
    def next_item(self):
        current = self.seq[-1]
        possibles = range(current,2*current+1)
        for p in self.seq:
            possibles = [x for x in possibles if x%p != 0]
        return possibles[0]       

class Fibonacci(Sequence):
    def __init__(self,n=2):
        self.name = 'Fibonacci'
        self.starter_seq = [1,1]
        super().__init__(n)
    def next_item(self):
        return self.seq[-2] + self.seq[-1]

class Natural(Sequence):
    def __init__(self,n=1):
        self.name = 'Natural'
        self.starter_seq = [1]
        super().__init__(n)
    def next_item(self):
        return self.seq[-1]+1
