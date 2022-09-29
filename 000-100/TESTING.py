def largest_cluster(startup, process, maxp):

    i = 0
    max_cluster = 0
    cluster = []

    boot_power = 0
    sum_process_power = 0

    for i in range(len(startup)):

        cluster.append((startup[i], process[i]))

        boot_power = max(boot_power, process[i])
        sum_process_power = sum_process_power + process[i]
        process_power = sum_process_power * len(cluster)
        power = boot_power + process_power

        if power < maxp:
            max_cluster = max(max_cluster, len(cluster))

        while power > maxp and cluster:
            lost = cluster.pop(0)

            boot_power = max([0] + [c[0] for c in cluster[1:]])
            sum_process_power -= lost[1]
            process_power = sum_process_power * len(cluster)
            power = boot_power + process_power

    return max_cluster


s = [0] * 500 + [0] + [0] * 500
p = [0] * 500 + [0] + [0] * 500
m = 12

import time

t1 = time.perf_counter()
print(largest_cluster(s, p, m))
t2 = time.perf_counter()
print(t2 - t1)
