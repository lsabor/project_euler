from maths.sequences.special_sequences import PrimesSeq
from maths.sets.special_sets import isPrime

P = PrimesSeq()

print(len(P.seq))

seq = []
for n in range(2, 5_000_000):
    if not n % 100000:
        print(n)
    if isPrime(n):
        seq.append(n)

P.seq = seq
P.expandCache()
print(len(P.seq))

P2 = PrimesSeq()
print(len(P2.seq))
