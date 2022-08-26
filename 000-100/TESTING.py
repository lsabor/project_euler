from maths.primes import divisorCount

best = 1
tmax = 0
for i in range(1001):
    t = divisorCount(i)
    if t > tmax:
        tmax = t
        best = i
print(print(best, tmax))
