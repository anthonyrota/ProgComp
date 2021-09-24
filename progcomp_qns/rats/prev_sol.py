from collections import defaultdict


def iterate(n):
    return int("".join(sorted(str(n + int(str(n)[::-1])))))


def serialize_cycle(cycle):
    return " ".join(str(n) for n in cycle)


def sort_cycle_smallest_member_first(cycle):
    smallest_member = min(cycle)
    smallest_member_idx = cycle.index(smallest_member)
    return cycle[smallest_member_idx:] + cycle[:smallest_member_idx]


cycle_counts = defaultdict(int)
cycles = []


def add_cycle(cycle_unsorted):
    cycle = sort_cycle_smallest_member_first(cycle_unsorted)
    serialized = serialize_cycle(cycle)
    if cycle_counts[serialized] == 0:
        cycles.append(cycle)
    cycle_counts[serialized] += 1


stop_value = 10**12
for i in range(1, 10000):
    n = i
    ns = [n]
    while True:
        n = iterate(n)
        if n == ns[-1]:
            add_cycle([n])
            break
        if n > stop_value:
            break
        if n in ns:
            idx = ns.index(n)
            cycle = ns[idx:]
            add_cycle(cycle)
            break
        ns.append(n)

cycles.sort(key=lambda cycle: (len(cycle), cycle[0]))
for cycle in cycles:
    serialized = serialize_cycle(cycle)
    print(
        f'Period: {len(cycle)}, occurs {cycle_counts[serialized]} times, cycle: {serialized}')
