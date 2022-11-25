from maths.graphs import *
import itertools as itt

import time

np.random.seed(1)

n = 3000
adjs = np.zeros((n, n, 2))
nodes = np.array([Node(i) for i in range(n)])
# add a connected subgraph of size k
k = 100
K = np.random.choice(range(n), k, replace=False)
for i, j in itt.combinations(K, 2):
    adjs[i, j, 0] = adjs[j, i, 0] = 1

# # adding random other edges
# for _ in range((n // 2) + 1):
#     i, j = np.random.choice(range(n), 2, replace=False)
#     adjs[i, j, 0] = adjs[j, i, 0] = 1

g = Graph(nodes=nodes, adjs=adjs)

t1 = time.perf_counter()

am = g.adjs[:, :, 0]
a1 = np.triu(am)
a2 = a1 @ a1
a3 = a1 * a2
# print(a1)
# print(a2)
# print(a3)
# print()

t2 = time.perf_counter()

triangles0 = []

for i, j in np.array(np.nonzero(a3)).T:
    ks = np.nonzero((a3[i] * a3[j])[j + 1 :])[0]
    for k in ks + j + 1:
        triangles0.append([i, j, k])


t3 = time.perf_counter()

# triangles1 = []
# for i, j in itt.combinations(range(n), 2):
#     # when a coordinate is non-zero, we have a triangle
#     if a3[i, j] > 0:
#         # test for other connections with later nodes
#         ks = np.where(a3[i, j + 1 :] * a3[j, j + 1 :] > 0)[0]
#         for k in ks + j + 1:
#             triangles1.append([i, j, k])

# t2 = time.perf_counter()

print(len(triangles0))
print(t2 - t1, "setup matricies")
print(t3 - t2, "find triangles")
# print(triangles1)
# print(t2 - t1)
