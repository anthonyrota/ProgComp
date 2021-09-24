from collections import defaultdict


def gen(n):
    return int(''.join(sorted(str(n + int(''.join(reversed(str(n))))))))


cycles = defaultdict(int)


def stringify_cycle(cycle):
    smallest = min(cycle)
    smallest_idx = cycle.index(smallest)
    c = cycle[smallest_idx:] + cycle[:smallest_idx]
    return ' '.join(str(x) for x in c)


stop = 10**12

for i in range(1, 10000):
    x = i
    nums = [x]
    while True:
        x = gen(x)
        if x in nums:
            x_idx = nums.index(x)
            cycle = nums[x_idx:]
            cycles[stringify_cycle(cycle)] += 1
            break
        nums.append(x)
        if x > stop:
            break

cycles_ = list(cycles.items())
cycles_.sort(key=lambda x: (len(x[0].split(' ')), x[0]))
for cycle in cycles_:
    print(
        f'Period: {len(cycle[0].split(" "))}, occurs {cycle[1]} times, cycle: {cycle[0]}')
