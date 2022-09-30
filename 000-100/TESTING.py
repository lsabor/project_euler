from maths.sequences.special_sequences import PrimesSeq
from maths.sets.special_sets import isPrime

P = PrimesSeq()

for i in range(5, 1000, 5):
    P.takeWhileLT(i * 100000)
    print(i, len(P.seq))
